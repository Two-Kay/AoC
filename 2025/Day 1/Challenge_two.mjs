let dialPosition = 50
let password = 0
function rotateDial(input) {
    const startingPosition = dialPosition
    const direction = input.substring(0, 1)
    const steps = parseInt(input.substring(1, input.length))
    if (direction === "L") {
        dialPosition -= steps
    }
    else {
        dialPosition += steps
    }
    password += Math.floor(Math.abs(dialPosition / 100))
    dialPosition %= 100
    if (dialPosition < 0) {
        dialPosition += 100
        if (startingPosition !== 0) {
            password += 1
        }
    }
    else if (dialPosition === 0 && direction === "L") {
        password += 1
    }
}

import { open } from 'node:fs/promises';
async function readInputContent() {
    const file = await open('./input');
    for await (const line of file.readLines()) {
        rotateDial(line)
    }
}
await readInputContent()
console.log(password)