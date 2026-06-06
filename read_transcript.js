const fs = require('fs');
const readline = require('readline');

async function extract() {
    const fileStream = fs.createReadStream('C:\\Users\\shrinidhi\\.gemini\\antigravity\\brain\\0fd962f3-918a-464a-92ad-843a458fd848\\.system_generated\\logs\\transcript.jsonl');
    const rl = readline.createInterface({ input: fileStream, crlfDelay: Infinity });

    let matchCount = 0;
    for await (const line of rl) {
        if (line.includes('mango-testing.html') && line.includes('img src=')) {
            try {
                const parsed = JSON.parse(line);
                if (parsed.output || parsed.content) {
                    console.log(line.substring(0, 500)); // Print just to verify we found something
                }
            } catch(e) {}
        }
    }
}
extract();
