/** Display values from recipe range */
let cookInput = document.getElementById('cook_time');
let cookOutput = document.getElementById('cookValOut');
let prepInput = document.getElementById('prep_time');
let prepOutput = document.getElementById('prepValOut');
let portionInput = document.getElementById('portions');
let portionOutput = document.getElementById('portionValOut');
displayRangeValue(cookInput, cookOutput);
displayRangeValue(prepInput, prepOutput);
displayRangeValue(portionInput, portionOutput);

function displayRangeValue(i,o) {
    o.value = i.value;
}