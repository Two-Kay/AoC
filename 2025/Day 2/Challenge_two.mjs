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
    let divisor = 2
    while (divisor <= idLength) {
        if (idLength % divisor === 0) {
            let idSplit = []
            for (let i = 0; i < divisor; i++) {
                idSplit.push(id.substring(i * (idLength / divisor), (i + 1) * (idLength / divisor)))
            }
            if (new Set(idSplit).size === 1) {
                return false
            }
        }
        divisor += 1
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