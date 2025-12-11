let junctions = []
let junctionClusters = []

async function clusterNJunctions(connectionCount) {
    let lastSmallestDistance = 10 ** 1000
    for (let i = 0; i < connectionCount; i++) {
        let smallestDistance = 10 ** 1000
        let closestPairIndices = null
        let closestClusterIndex = -1
        let clusterMerge = false
        let skipThis = false
        for (const selectedIndex in junctions) {
            for (const comparsionIndex in junctions) {
                if (comparsionIndex !== selectedIndex) {
                    const distance = computeDistance(junctions[selectedIndex], junctions[comparsionIndex])
                    if (distance < smallestDistance) {
                        smallestDistance = distance
                        closestPairIndices = [selectedIndex, comparsionIndex]
                        closestClusterIndex = -1
                    }
                }
            }
            for (const clusterIndex in junctionClusters) {
                for (const junctionIndex in junctionClusters[clusterIndex]) {
                    const distance = computeDistance(junctions[selectedIndex], junctionClusters[clusterIndex][junctionIndex])
                    if (distance < smallestDistance) {
                        smallestDistance = distance
                        closestPairIndices = [selectedIndex, clusterIndex]
                        closestClusterIndex = clusterIndex
                    }
                }
            }
        }
        for (const clusterIndex in junctionClusters) {
            for (const clusterIndexComp in junctionClusters) {
                if (clusterIndex !== clusterIndexComp) {
                    for (const selectedIndex in junctionClusters[clusterIndex]) {
                        for (const comparsionIndex in junctionClusters[clusterIndexComp]) {
                            const distance = computeDistance(junctionClusters[clusterIndex][selectedIndex], junctionClusters[clusterIndexComp][comparsionIndex])
                            if (distance < smallestDistance) {
                                smallestDistance = distance
                                closestPairIndices = [clusterIndex, clusterIndexComp]
                                clusterMerge = true
                            }
                        }
                    }
                }
            }
        }
        for (const clusterIndex in junctionClusters) {
            for (const selectedIndex in junctionClusters[clusterIndex]) {
                for (const comparsionIndex in junctionClusters[clusterIndex]) {
                    if (selectedIndex !== comparsionIndex) {
                        const distance = computeDistance(junctionClusters[clusterIndex][selectedIndex], junctionClusters[clusterIndex][comparsionIndex])
                        if (distance > lastSmallestDistance && distance < smallestDistance) {
                            smallestDistance = distance
                            skipThis = true
                        }
                    }
                }
            }
        }
        if (!skipThis) {
            if (clusterMerge) {
                for (const junction of junctionClusters[closestPairIndices[1]]) {
                    junctionClusters[closestPairIndices[0]].push(junction)
                }
                junctionClusters.splice(closestPairIndices[1], 1)
                lastSmallestDistance = smallestDistance
            }
            else if (closestClusterIndex >= 0) {
                junctionClusters[closestClusterIndex].push(junctions[closestPairIndices[0]])
                junctions.splice(closestPairIndices[0], 1)
                lastSmallestDistance = smallestDistance
            }
            else {
                junctionClusters.push([junctions[closestPairIndices[0]], junctions[closestPairIndices[1]]])
                if (parseInt(closestPairIndices[1]) > parseInt(closestPairIndices[0])) {
                    junctions.splice(closestPairIndices[1], 1)
                    junctions.splice(closestPairIndices[0], 1)
                }
                else {
                    junctions.splice(closestPairIndices[0], 1)
                    junctions.splice(closestPairIndices[1], 1)
                }
                lastSmallestDistance = smallestDistance
            }
        }
        else {
            lastSmallestDistance = smallestDistance
        }
    }
}

function computeDistance(junctionStart, junctionEnd) {
    return (Math.sqrt((junctionStart[0] - junctionEnd[0]) ** 2 + (junctionStart[1] - junctionEnd[1]) ** 2 + (junctionStart[2] - junctionEnd[2]) ** 2))
}

import { open } from 'node:fs/promises';
async function readInputContent() {
    const file = await open('./input');
    for await (const line of file.readLines()) {
        let junction = line.split(',')
        for (const coordinate in junction) {
            junction[coordinate] = parseInt(junction[coordinate])
        }
        junctions.push(junction)
    }
}

await readInputContent()
await clusterNJunctions(1000)
let biggestCluster = 0
let secondBiggestCluster = 0
let thirdBiggestCluster = 0
for (const cluster of junctionClusters) {
    const size = cluster.length
    if (size > biggestCluster) {
        thirdBiggestCluster = secondBiggestCluster
        secondBiggestCluster = biggestCluster
        biggestCluster = size
    }
    else if (size > secondBiggestCluster) {
        thirdBiggestCluster = secondBiggestCluster
        secondBiggestCluster = size
    }
    else if (size > thirdBiggestCluster) [
        thirdBiggestCluster = size
    ]
}
console.log(biggestCluster * secondBiggestCluster * thirdBiggestCluster)