function solution(n, lost, reserve) {
    var new_lost = lost.filter(x => !reserve.includes(x));
    reserve = reserve.filter(x => !lost.includes(x));
    lost = new_lost.slice();
    
    var idx = 0;
    for (var i = 0; i < lost.length; i++) {
        if (reserve.includes(lost[i] - 1)) {
            idx = reserve.indexOf(lost[i] - 1);
            reserve.splice(idx, 1);
        } else if (reserve.includes(lost[i] + 1)) {
            idx = reserve.indexOf(lost[i] + 1);
            reserve.splice(idx, 1);
        } else {
            continue;
        }
        
        idx = new_lost.indexOf(lost[i]);
        new_lost.splice(idx, 1);
    }
    
    return n - new_lost.length;
}

console.log(solution(4, [3, 1, 2], [2, 4, 3]), 3);