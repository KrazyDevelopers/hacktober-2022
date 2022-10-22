/**
 * Get the minmum and maximum element of the array
 * @param {number[]} array The array of number
 * @param {"array" | "object"} returnFormat return format
 */
module.exports = function array_min_max(array, returnFormat = "object") {
    let min = {
        value: array[0],
        index: 0
    }, max = {
        value: array[0],
        index: 0
    };

    for (let i = 0; i < array.length; i++) {
        if (array[i] < min.value) min = {
            value: array[i],
            index: i
        }

        if (array[i] > max.value) max = {
            value: array[i],
            index: i
        }
    }

    return returnFormat === "object" ? { min, max } : [min, max]
}