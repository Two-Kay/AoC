let quantumTachyonManifold = []

async function identifyStart() {
    for (let x = 0; x < quantumTachyonManifold.length; x++) {
        if (quantumTachyonManifold[0][x] === "S") {
            quantumTachyonManifold[1][x] = "|"
            return x
        }
    }
    return 0
}

function computeTimeline(tachyonManifold, y, x, nodeMap) {
    let timelineCount = 0
    while (y < (tachyonManifold.length - 1)) {
        if (tachyonManifold[y + 1][x] === "^") {
            if (nodeMap.has(x + '-' + (y + 1))) {
                timelineCount = nodeMap.get(x + '-' + (y + 1))
                return timelineCount
            }
            let leftTachyonManifold = []
            for (var i = 0; i < tachyonManifold.length; i++)
                leftTachyonManifold[i] = tachyonManifold[i].slice();
            let rightTachyonManifold = []
            for (var i = 0; i < tachyonManifold.length; i++)
                rightTachyonManifold[i] = tachyonManifold[i].slice();
            leftTachyonManifold[y + 1][x - 1] = "|"
            rightTachyonManifold[y + 1][x + 1] = "|"
            timelineCount += computeTimeline(leftTachyonManifold, y + 1, x - 1, nodeMap)
            timelineCount += computeTimeline(rightTachyonManifold, y + 1, x + 1, nodeMap)
            nodeMap.set(x + '-' + (y + 1), timelineCount)
            return timelineCount
        }
        else {
            tachyonManifold[y + 1][x] = "|"
        }
        y += 1
    }
    return 1
}

import { open } from 'node:fs/promises';
async function readInputContent() {
    const file = await open('./input');
    for await (const line of file.readLines()) {
        quantumTachyonManifold.push(Array.from(line))
    }
}

await readInputContent()
let x = await identifyStart()
const map = new Map()
console.log(computeTimeline(quantumTachyonManifold, 1, x, map))