let redTileCoords = []
let redTileCoordString = []

function getBiggestRectangle() {
    let biggestPair = []
    let maxArea = 0
    for (let i = 0; i < redTileCoords.length - 1; i++) {
        for (let j = i + 1; j < redTileCoords.length; j++) {
            let x = Math.min(redTileCoords[i][0], redTileCoords[j][0]) + 1
            let startY = Math.min(redTileCoords[i][1], redTileCoords[j][1]) + 1
            let y = startY
            let endX = Math.max(redTileCoords[i][0], redTileCoords[j][0])
            let endY = Math.max(redTileCoords[i][1], redTileCoords[j][1])
            const area = (endX - (x - 2)) * (endY - (y - 2))
            if (area > maxArea) {
                maxArea = area
                biggestPair = [redTileCoords[i], redTileCoords[j]]
            }
        }
    }
    return maxArea
}

import { open } from 'node:fs/promises';
async function readInputContent() {
    const file = await open('./input');
    for await (const line of file.readLines()) {
        redTileCoords.push(line.split(',').map(Number));
        redTileCoordString.push(line)
    }
}

await readInputContent()
console.log(getBiggestRectangle())