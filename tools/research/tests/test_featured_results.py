"""Keep leading results ordered, scoped and derived from reviewable metadata."""
import copy
import unittest
from unittest.mock import patch

from tools.research import navigation, registry


def result(ident, status='reviewed-scoped'):
    return {
        'id': ident, 'status': status, 'kind': 'argument',
        'title': {'zh': ident + ' 主张', 'en': ident + ' claim'},
        'canonical_source': 'theories/' + ident + '.md',
        '_record_path': 'theories/results/records/' + ident + '.json',
        'dependencies': [],
        'overview': {
            'title': {'zh': ident + ' 标题', 'en': ident + ' result'},
            'summary': {'zh': ident + ' 摘要', 'en': ident + ' scoped summary'},
            'evidence': {'zh': ident + ' 证据', 'en': ident + ' recorded evidence'},
        },
    }


def goal(ident, result_ids=()):
    return {
        'id': ident, 'scope_type': 'project-direction',
        **{field: {'zh': ident + ' ' + field, 'en': ident + ' ' + field}
           for field in ('title', 'scope', 'objective', 'completion', 'premises')},
        'sources': ['README.md'], 'result_ids': list(result_ids),
        'overview': {
            'title': {'zh': ident + ' 方向', 'en': ident + ' direction'},
            'summary': {'zh': ident + ' 研究', 'en': ident + ' research summary'},
            'next_step': {'zh': ident + ' 下一步', 'en': ident + ' next investigation'},
        },
    }


class FeaturedResultsTests(unittest.TestCase):
    def test_selection_is_optional_and_preserves_configured_order(self):
        records = [result('first'), result('second')]
        self.assertEqual(navigation.featured_results(records, {}), [])
        selected = navigation.featured_results(records, {'readme_featured_results': ['second', 'first']})
        self.assertEqual([r['id'] for r in selected], ['second', 'first'])

    def test_rejects_malformed_duplicate_and_missing_selections(self):
        records = [result('first')]
        for configured, message in [
            ('first', 'list of result IDs'),
            ([3], 'list of result IDs'),
            (['first', 'first'], 'duplicate result IDs'),
            (['missing'], 'missing result'),
        ]:
            with self.subTest(configured=configured):
                with self.assertRaisesRegex(ValueError, message):
                    navigation.featured_results(records, {'readme_featured_results': configured})

    def test_rejects_open_superseded_and_withdrawn_results(self):
        for status in ('open', 'superseded', 'withdrawn'):
            with self.subTest(status=status):
                with self.assertRaisesRegex(ValueError, 'completed scoped result'):
                    navigation.featured_results([result('first', status)], {'readme_featured_results': ['first']})

    def test_rejects_target_even_if_incorrectly_marked_completed(self):
        record = result('first')
        record['kind'] = 'target'
        with self.assertRaisesRegex(ValueError, 'completed scoped result'):
            navigation.featured_results([record], {'readme_featured_results': ['first']})

    def test_requires_all_bilingual_overview_fields(self):
        for field in ('title', 'summary', 'evidence'):
            for language in ('en', 'zh'):
                record = result('first')
                record['overview'][field][language] = ' '
                with self.subTest(field=field, language=language):
                    with self.assertRaisesRegex(ValueError, 'bilingual overview'):
                        navigation.featured_results([record], {'readme_featured_results': ['first']})

    def test_navigation_validation_reports_invalid_featured_selection(self):
        with patch.object(navigation, 'goals', return_value=[]), patch.object(navigation, 'read', return_value={'readme_featured_results': ['missing']}):
            errors = navigation.validate_goals([])
        self.assertTrue(any('missing result: missing' in error for error in errors))

    def test_root_leads_with_ordered_english_summaries_and_source_links(self):
        records = [result('first'), result('second')]
        config = {'readme_featured_results': ['second', 'first']}
        def read(path):
            return config if path == navigation.CONFIG else {'documents': {}}
        with patch.object(navigation, 'read', side_effect=read), patch.object(navigation, 'goals', return_value=[]):
            views = navigation.render_views(records)
        root = views['README.md']
        self.assertTrue(root.startswith('# The Theory of Becoming\n'))
        self.assertLess(root.index('### second result'), root.index('### first result'))
        self.assertLess(root.index('first recorded evidence'), root.index('## Research and repository'))
        self.assertIn('second scoped summary', root)
        self.assertIn('[Canonical source](theories/second.md)', root)
        self.assertIn('[Scope, premises and evidence](theories/results/records/second.md)', root)
        self.assertNotIn('second 摘要', root)
        self.assertNotIn('我们研究同一生成展开', root)
        self.assertIn('我们研究同一生成展开', views['_process/BRIEF.md'])
        self.assertNotIn('## Leading results', views['_process/BRIEF.md'])

    def test_optional_overview_is_validated_and_visible_on_record_page(self):
        records, _ = registry.load_records()
        record = copy.deepcopy(records[0])
        record['overview'] = result('editorial')['overview']
        rendered = registry.render_record(record)
        for field in ('title', 'summary', 'evidence'):
            for language in ('en', 'zh'):
                self.assertIn(record['overview'][field][language], rendered)
        for bad in (None, {}, {'title': {'zh': '标题', 'en': 'Title'}}):
            record['overview'] = bad
            errors, _ = registry.validate([record])
            self.assertTrue(any('overview requires bilingual' in error for error in errors))


class ResearchGoalsTests(unittest.TestCase):
    def test_selection_is_optional_and_ordered(self):
        goals = [goal('ethics'), goal('evolution')]
        self.assertEqual(navigation.research_goals(goals, {}), [])
        selected = navigation.research_goals(goals, {'readme_research_goals': ['evolution', 'ethics']})
        self.assertEqual([g['id'] for g in selected], ['evolution', 'ethics'])

    def test_rejects_malformed_duplicate_and_missing_goal_ids(self):
        for configured, message in [
            ('ethics', 'list of goal IDs'),
            ([3], 'list of goal IDs'),
            (['ethics', 'ethics'], 'duplicate goal IDs'),
            (['unknown'], 'missing goal'),
        ]:
            with self.subTest(configured=configured):
                with self.assertRaisesRegex(ValueError, message):
                    navigation.research_goals([goal('ethics')], {'readme_research_goals': configured})

    def test_rejects_missing_translation_and_validates_unselected_overview(self):
        for field in ('title', 'summary', 'next_step'):
            for language in ('en', 'zh'):
                metadata = goal('ethics')
                metadata['overview'][field][language] = ' '
                with self.subTest(field=field, language=language):
                    with self.assertRaisesRegex(ValueError, 'bilingual overview'):
                        navigation.research_goals([metadata], {'readme_research_goals': ['ethics']})
                    with patch.object(navigation, 'goals', return_value=[metadata]), patch.object(navigation, 'read', return_value={}):
                        errors = navigation.validate_goals([])
                    self.assertTrue(any('overview requires bilingual' in error for error in errors))

    def test_navigation_validation_reports_missing_goal_id(self):
        with patch.object(navigation, 'goals', return_value=[]), patch.object(navigation, 'read', return_value={'readme_research_goals': ['unknown']}):
            errors = navigation.validate_goals([])
        self.assertTrue(any('missing goal: unknown' in error for error in errors))

    def test_root_renders_ordered_research_and_only_established_result_links(self):
        records = [result('checked', 'recorded-checked'), result('reviewed'), result('open-result', 'open'), result('retired', 'superseded'), result('withdrawn-result', 'withdrawn')]
        records[2]['kind'] = 'target'
        goals = [goal('ethics', ['open-result', 'checked', 'retired', 'reviewed', 'withdrawn-result']), goal('evolution')]
        config = {'readme_featured_results': ['checked'], 'readme_research_goals': ['evolution', 'ethics']}
        def read(path):
            return config if path == navigation.CONFIG else {'documents': {}}
        with patch.object(navigation, 'read', side_effect=read), patch.object(navigation, 'goals', return_value=goals):
            views = navigation.render_views(records)
        root = views['README.md']
        self.assertLess(root.index('## Leading results'), root.index('## Ongoing research and current progress'))
        self.assertLess(root.index('### evolution direction'), root.index('### ethics direction'))
        self.assertLess(root.index('### ethics direction'), root.index('## Research and repository'))
        self.assertIn('**Next:** ethics next investigation', root)
        self.assertIn('[Scope and authorization](GOALS.md#ethics)', root)
        self.assertIn('[Primary source](README.md)', root)
        established = next(line for line in root.splitlines() if line.startswith('**Established results:**'))
        self.assertIn('[checked claim](theories/results/records/checked.md)', established)
        self.assertIn('[reviewed claim](theories/results/records/reviewed.md)', established)
        self.assertNotIn('open-result', established)
        self.assertNotIn('retired', established)
        self.assertNotIn('withdrawn-result', established)
        self.assertNotIn('ethics 研究', root)
        self.assertIn('ethics 研究', views['GOALS.md'])
        self.assertIn('ethics 下一步', views['GOALS.md'])


if __name__ == '__main__':
    unittest.main()
