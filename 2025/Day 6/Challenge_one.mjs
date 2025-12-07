let numbers = []
let operations = []

function solveMathPuzzle() {
    let sum = 0
    for (let i = 0; i < numbers[0].length; i++) {
        let storage = 0
        for (let j = 0; j < numbers.length; j++) {
            if (operations[i] === "+") {
                storage += numbers[j][i]
            }
            else if (operations[i] === "*") {
                if (storage === 0) {
                    storage += 1
                }
                storage *= numbers[j][i]
            }
        }
        sum += storage
    }
    return sum
}

import { open } from 'node:fs/promises';
async function readInputContent() {
    const file = await open('./input');
    let isOperation = false
    for await (const line of file.readLines()) {
        const re = /\s+/;
        const lineList = line.split(re);
        if (line.includes('*') || line.includes('+')) {
            isOperation = true
        }
        if (!isOperation) {
            numbers.push(lineList.filter(n => n).map(Number))
        }
        else {
            operations = lineList.filter(n => n)
        }
    }
}

await readInputContent()
console.log(solveMathPuzzle())