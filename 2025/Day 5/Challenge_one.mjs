let freshnessRanges = []
let ingredients = []

function countFreshItems() {
    let count = 0
    for (const ingredient of ingredients) {
        for (const freshnessRange of freshnessRanges) {
            if (parseInt(ingredient) >= parseInt(freshnessRange[0]) && parseInt(ingredient) <= parseInt(freshnessRange[1])) {
                count++
                break;
            }
        }
    }
    return count
}

import { open } from 'node:fs/promises';
async function readInputContent() {
    const file = await open('./input');
    let isIngredients = false
    for await (const line of file.readLines()) {
        if (line.length === 0) {
            isIngredients = true
        }
        else {
            if (!isIngredients) {
                freshnessRanges.push(line.split('-'))
            }
            else {
                ingredients.push(line)
            }
        }
    }
}

await readInputContent()
console.log(countFreshItems())