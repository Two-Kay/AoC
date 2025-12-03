let joltages = []

function computeJoltages() {
    let joltageSum = BigInt(0)
    for (const joltage of joltages) {
        let eliminationJoltage = joltage
        while (eliminationJoltage.length > 12) {
            let biggestJoltage = BigInt(eliminationJoltage.substring(0, (eliminationJoltage.length - 1)))
            for (let i = 0; i < eliminationJoltage.length; i++) {
                const testJoltage = BigInt(eliminationJoltage.substring(0, i) + eliminationJoltage.substring(i + 1))
                if (testJoltage > biggestJoltage) {
                    biggestJoltage = testJoltage
                }
            }
            eliminationJoltage = biggestJoltage.toString()
        }
        joltageSum += BigInt(eliminationJoltage)
    }
    return joltageSum
}

import { open } from 'node:fs/promises';
async function readInputContent() {
    const file = await open('./input');
    for await (const line of file.readLines()) {
        joltages.push(line)
    }
}

await readInputContent()
console.log(computeJoltages())