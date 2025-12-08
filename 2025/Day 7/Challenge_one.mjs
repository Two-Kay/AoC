let tachyonManifold = []

function splitTachyonBeam() {
    let splitCount = 0
    for (let y = 0; y < tachyonManifold.length - 1; y++) {
        for (let x = 0; x < tachyonManifold[y].length; x++) {
            if (tachyonManifold[y][x] === "|" || tachyonManifold[y][x] === "S") {
                if (tachyonManifold[y + 1][x] === "^") {
                    tachyonManifold[y + 1][x + 1] = "|"
                    tachyonManifold[y + 1][x - 1] = "|"
                    splitCount += 1
                }
                else {
                    tachyonManifold[y + 1][x] = "|"
                }
            }
        }
    }
    return splitCount
}

import { open } from 'node:fs/promises';
async function readInputContent() {
    const file = await open('./input');
    for await (const line of file.readLines()) {
        tachyonManifold.push(Array.from(line))
    }
}

await readInputContent()
console.log(splitTachyonBeam())