let joltages = []

function computeJoltages() {
    let joltageSum = 0
    for (const joltage of joltages) {
        let highestJoltage = "00"
        let highestDigit = 0
        for (const digit of joltage) {
            const altJoltage = parseInt(highestDigit.toString() + digit)
            if (altJoltage > parseInt(highestJoltage)) {
                highestJoltage = altJoltage.toString()
            }
            if (parseInt(digit) > highestDigit) {
                highestDigit = parseInt(digit)
            }
        }
        joltageSum += parseInt(highestJoltage)
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