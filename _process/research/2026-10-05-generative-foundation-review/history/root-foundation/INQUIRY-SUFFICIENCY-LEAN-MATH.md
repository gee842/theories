# Constructive sufficiency for an inquiry and its response

6 October 2026. AI-authored mathematical account for formal integration of the [existing sufficiency composition](INQUIRY-SUFFICIENCY-MATH.md). The connection is **actual inquiry changes continuing possibilities → a common executable response remains available on every possible acquired outcome**. This addresses the meaning and logical dependencies of a sufficiency criterion. It does not claim to form that criterion's practical significance, install it in a learner, or establish the stronger no-assumptions foundation.

## Preserve the whole relevant continuation

Use the existing generative `Process` interface. A query and a response occur through its actual step relation. Retained possibilities describe configurations of that process, including whatever their subsequent operation depends on. If the question concerns an initial identity, that label must remain attached to the changing configuration; two equal current configurations do not establish equal histories. The [identifying-inquiry study](../../../../theories/becoming/history/INQUIRY-AND-MATHEMATICAL-IDENTITY.md) supplies a concrete reason for this requirement.

Fix the represented observation interface, conditions on permitted intermediate steps, and endpoint requirement of the response. These are explicit local contracts, not assertions that all inquiry or ethical significance has this form. In particular, a terminal response is one executable finite action sequence, common to the still-compatible configurations. Every admitted execution of that sequence must preserve the intermediate conditions and end with the declared requirement. The sequence must be executable from every candidate; a dead end is not success by vacuity.

For a candidate predicate \(B\), an inquiry action \(a\) and acquired observation \(o\), retain

\[
B_{a,o}(t)\iff \exists s,\; B(s)\land P(s,a,t)\land \operatorname{sense}(s,a,t)=o.
\]

This propagates the configurations before filtering the observation. It includes every actual successor compatible with that observation. An inquiry is admitted only if each current candidate has a successor and every successor satisfies the declared intermediate condition. The unchanged actual process determines these effects. A query that is disabled in one candidate may not discard that candidate as though silence had identified another one.

## Finite policies and the constructive recurrence

A policy is an independently specified finite tree: it either terminates with a common response or issues an action and selects the next tree from its observed outcome. An abort leaf represents an impossible branch only. The maximum number of inquiry actions is uniformly bounded; the terminal response retains its own action sequence and conditions.

Let \(W_n(B)\) describe usable sufficiency with at most \(n\) inquiries. Its live configurations must be nonempty. At depth zero, a common total response must exist. At the next depth there is either such a response now, or an admitted action whose every observation branch comes with one of the following:

\[
\operatorname{Empty}(B_{a,o})\quad\lor\quad W_n(B_{a,o}).
\]

The empty branch is not permission to act. It says there is no actual successor that can enter that branch. For a real current configuration and admitted action, some successor exists and belongs to its acquired observation branch, ruling out that branch's empty alternative.

**Bounded-policy characterization.** This constructive recurrence holds exactly when a finite policy of the indicated depth correctly handles every current candidate and every subsequent actual outcome under the stated contracts.

The proof is by the depth and policy structure. A common response gives a terminal policy. For an inquiry, each of the finitely many observations supplies either an impossible-branch abort or a smaller correct policy. Finite induction assembles those policies into one branching tree; no unrestricted choice operator is needed. Conversely, inspect a correct tree: its terminal case supplies the common response, while its query case supplies admission and the smaller branch certificates. On a live actual history, each observed successor remains among the candidates and satisfies the intermediate condition, so following the tree reaches a certified executable response within the bound.

This is stronger than finding a favorable trace and different from requiring a separate hidden-state-dependent response for each candidate. It also differs from claiming probability-one eventual success: the bound and guarantee cover every admitted finite branch.

## Why the branch formulation matters

The earlier hand proof writes the branch obligation as

\[
\operatorname{Nonempty}(B_{a,o})\to W_n(B_{a,o}).
\]

For a finite executable representation, branch nonemptiness can be decided from the represented candidates and their successors. In that setting the implication and explicit empty/live alternatives agree. But merely declaring finitely many observation labels does not decide whether an arbitrary predicate on an arbitrary state type has a witness. Moving from the implication to a usable branch policy without that distinction can conceal excluded middle or choice.

The formal integration therefore retains the constructive branch certificate and separately identifies when finite representation discharges its classification requirement. It must not claim unconditional constructive equivalence between the two branch formulations for arbitrary undecidable predicates. No generic computable decision procedure follows from a theorem about arbitrary `Process` relations.

## Substantive controls

1. A singleton candidate set with no executable adequate response fails the response criterion, even though identification is complete.
2. Several candidates sharing one executable adequate response can suffice, even while their historical identities remain unresolved.
3. A truthful observation can leave candidate count unchanged while changing subsequent possibilities. The existing `010` history gives exactly this distinction for predictions.
4. An informative inquiry can consume the only condition needed for another test or for the terminal response. Its bad successor must remain in the guarantee. The one-source access history demonstrates this for identification.
5. An action disabled at one candidate is not a universally available experiment. It cannot succeed by deleting that case.
6. An empty candidate set indicates that the current application has no live represented situation. It cannot establish warranted action for a real situation.

These are constraints on the reconstructed activity and the claim made about it. They neither add a scalar reward nor define all adaptive change as wisdom. The observation interface's actual acquisition and calibration remain separate implementation obligations; ethical uses additionally require justified contracts.

## Relation to the newer criterion-revision implementation

The concurrently developed [inquiry-revision extension](../../../../theories/becoming/history/INQUIRY-REVISION.md) is already a positive construction of acquired evidence changing an operative encounter requirement. It explicitly adds a formation/read/rewrite law and retains false-positive, wrong-sign and affordability controls. Its own acceptance records govern that result.

The present theorem does not recreate that mechanism, import its law as a foundational premise, or declare its threshold warranted. It supplies a general criterion against which a proposed revised inquiry can be assessed: retain all its actual successors, require an available common response, and preserve the pertinent intermediate conditions. The particular interpretation, authority and formation or selection of its revision rule still need their own explanation within the common account.

V7.3 also distinguished bounded value from actual stopping: a bounded benefit can have a finite optimum for each positive cost while that optimum grows without bound as the cost approaches zero. The [preserved S6 result](../../../../drafts/2026-10-02-iaseai-selecting-the-selectors/v7.3/src/supp/06_S6.md#the-bounded-optimizer-section-64) does not derive an acquired stopping criterion. The present continuation interface does not import its scalar objective or threshold into the foundation. It integrates the relevant distinction while preserving the original mathematical scope.
