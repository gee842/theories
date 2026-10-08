// Read-only extraction. Run a copy beside a symlink to the bundled node_modules.
import fs from 'node:fs/promises';
import path from 'node:path';
import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
const [source, output] = process.argv.slice(2);
if (!source || !output) throw new Error('Expected source directory and output directory');
await fs.mkdir(output, { recursive: true });
for (const fig of [2,4]) {
 const file = `elife-65935-fig${fig}-data1-v2.xlsx`;
 const w = await SpreadsheetFile.importXlsx(await FileBlob.load(path.join(source,file)));
 const overview=(await w.inspect({kind:'sheet',include:'id,name',maxChars:2000})).ndjson;
 const sheet=w.worksheets.getItemAt(0);
 const data={file,sheet:sheet.name,values:sheet.getUsedRange().values};
 await fs.writeFile(path.join(output,`figure${fig}.json`),JSON.stringify(data,null,2)+'\n');
 console.log(overview);
}
