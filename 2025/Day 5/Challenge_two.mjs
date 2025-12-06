let freshnessRanges = []

function countFreshItemsRanges() {
    let count = 0
    for (const freshnessRange of freshnessRanges) {
        count += 1 + parseInt(freshnessRange[1]) - parseInt(freshnessRange[0])
    }
    return count
}

async function combineRanges() {
    let hasChange = false
    do {
        hasChange = false
        for (const range in freshnessRanges) {
            let indicesToDelete = []
            let newRange = freshnessRanges[range]
            let start = parseInt(freshnessRanges[range][0])
            let end = parseInt(freshnessRanges[range][1])
            for (const comparsionRange in freshnessRanges) {
                if (range !== comparsionRange) {
                    let compStart = parseInt(freshnessRanges[comparsionRange][0])
                    let compEnd = parseInt(freshnessRanges[comparsionRange][1])
                    if (start >= compStart && start <= compEnd && end >= compEnd) {
                        hasChange = true
                        newRange[0] = compStart.toString()
                        indicesToDelete.push(comparsionRange)
                        break;
                    }
                    else if (end >= compStart && end <= compEnd && start <= compStart) {
                        hasChange = true
                        newRange[1] = compEnd.toString()
                        indicesToDelete.push(comparsionRange)
                        break;
                    }
                    if (parseInt(newRange[1]) < compEnd && parseInt(newRange[0]) > compStart) {
                        hasChange = true
                        indicesToDelete.push(range)
                        break;
                    }
                }
            }
            if (hasChange) {
                freshnessRanges[range] = newRange
                for (let i = freshnessRanges.length - 1; i >= 0; i--) {
                    if (indicesToDelete.includes(i.toString())) {
                        freshnessRanges.splice(i, 1);
                    }
                }
                break;
            }
        }
    } while (hasChange)
}

import { open } from 'node:fs/promises';
async function readInputContent() {
    const file = await open('./input');
    for await (const line of file.readLines()) {
        if (line.length === 0) {
            break;
        }
        else {
            freshnessRanges.push(line.split('-'))
        }
    }
}

await readInputContent()
await combineRanges()
console.log(countFreshItemsRanges())