let shelf = []

function countMovablePaperRolls() {
    let movable = 0
    for (const shelfRow in shelf) {
        const row = parseInt(shelfRow)
        for (const position in shelf[row]) {
            let adjacent = 0
            const pos = parseInt(position)
            if (shelf[row][pos] !== ".") {
                if (pos !== 0) {
                    if (shelf[row][pos - 1] !== ".") {
                        adjacent += 1
                    }
                    if (row !== 0) {
                        if (shelf[row - 1][pos - 1] !== ".") {
                            adjacent += 1
                        }
                    }
                    if (row !== shelf.length - 1) {
                        if (shelf[row + 1][pos - 1] !== ".") {
                            adjacent += 1
                        }
                    }
                }
                if (pos !== shelf[row].length - 1) {
                    if (shelf[row][pos + 1] !== ".") {
                        adjacent += 1
                    }
                    if (row !== 0) {
                        if (shelf[row - 1][pos + 1] !== ".") {
                            adjacent += 1
                        }
                    }
                    if (row !== shelf.length - 1) {
                        if (shelf[row + 1][pos + 1] !== ".") {
                            adjacent += 1
                        }
                    }
                }
                if (row !== 0) {
                    if (shelf[row - 1][pos] !== ".") {
                        adjacent += 1
                    }
                }
                if (row !== shelf.length - 1) {
                    if (shelf[row + 1][pos] !== ".") {
                        adjacent += 1
                    }
                }
                if (adjacent < 4) {
                    shelf[row][pos] = 'x'
                    movable += 1
                }
            }
        }
    }
    for (const row of shelf) {
        console.log(row)
    }
    return movable
}

import { open } from 'node:fs/promises';
async function readInputContent() {
    const file = await open('./input');
    for await (const line of file.readLines()) {
        shelf.push(Array.from(line))
    }
}

await readInputContent()
console.log(countMovablePaperRolls())