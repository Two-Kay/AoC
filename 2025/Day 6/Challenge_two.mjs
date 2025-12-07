let numbers = []
let operations = []

function solveMathPuzzle() {
    let sum = 0
    for (let i = 0; i < operations.length; i++) {
        let storage = 0
        if (operations[i] === "+") {
            for (const number of numbers[i]) {
                storage += number
            }
        }
        else if (operations[i] === "*") {
            if (storage === 0) {
                storage = 1
            }
            for (const number of numbers[i]) {
                storage *= number
            }
        }
        sum += storage
    }
    return sum
}

async function rotateNumbers() {
    let rotatedMatrix = numbers[0].map((val, index) => numbers.map(row => row[row.length - 1 - index]));
    let newNumbers = []
    let columnToAdd = []
    for (const row of rotatedMatrix) {
        let number = row.join('').trim()
        if (number === '') {
            newNumbers.push(columnToAdd)
            columnToAdd = []
        }
        else {
            columnToAdd.push(parseInt(number))
        }
    }
    newNumbers.push(columnToAdd)
    return newNumbers
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
            numbers.push(Array.from(line))
        }
        else {
            operations = lineList.filter(n => n).reverse()
        }
    }
}

await readInputContent()
numbers = await rotateNumbers()
console.log(solveMathPuzzle())