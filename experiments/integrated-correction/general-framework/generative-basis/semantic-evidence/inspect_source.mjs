// Read-only extraction. Run with the bundled @oai/artifact-tool available to Node.
import fs from 'node:fs/promises';
import path from 'node:path';
import {FileBlob, SpreadsheetFile} from '@oai/artifact-tool';

const [root, output] = process.argv.slice(2);
if (!root || !output) throw new Error('Usage: inspect_source.mjs REPOSITORY OUTPUT_DIRECTORY');
await fs.mkdir(output, {recursive:true});
for (const fig of [2, 3]) {
  const source = `sources/knowledge-semantics/elife-59998-fig${fig}-data1-v2.xlsx`;
  const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(path.join(root, source)));
  const summary = await workbook.inspect({kind:'workbook,sheet,table', maxChars:4500, tableMaxRows:6, tableMaxCols:8});
  const sheet = workbook.worksheets.getItemAt(0);
  const addresses = fig===2 ? ['B55:X72'] : ['B3:I11','B14:I23'];
  const record = {source, sheet:sheet.name, ranges:addresses.map(address => ({address, values:sheet.getRange(address).values}))};
  await fs.writeFile(path.join(output, `figure${fig}.json`), JSON.stringify(record,null,2)+'\n');
  await fs.writeFile(path.join(output, `figure${fig}-inspection.ndjson`),summary.ndjson+'\n');
  console.log(`Read ${source}: ${sheet.name}, ${addresses.join('; ')}`);
}
