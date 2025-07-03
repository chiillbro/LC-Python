import (
    "math/bits"
)

func kthCharacter(k int) byte {
    return byte(97 + bits.OnesCount(uint(k-1)))
}