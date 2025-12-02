let inputIds = [];

function coundWrongIds() {
    let invalidIdSum = 0
    for (const inputId of inputIds) {
        let checkId = parseInt(inputId[0])
        while (checkId <= inputId[1]) {
            if (!checkValid(checkId.toString())) {
                invalidIdSum += checkId
            }
            checkId += 1
        }
    }
    return invalidIdSum
}

function checkValid(id) {
    const idLength = id.length
    if (idLength % 2 === 0) {
        if (id.substring(0, idLength / 2) === id.substring(idLength / 2, idLength)) {
            return false
        }
    }
    return true
}

import { open } from 'node:fs/promises';
async function readInputContent() {
    const file = await open('./input');
    for await (const line of file.readLines()) {
        const idPairList = line.split(",")
        for (const idPair of idPairList) {
            if (idPair.length > 0) {
                inputIds.push(idPair.split('-'))
            }
        }
    }
}
await readInputContent()
console.log(coundWrongIds())