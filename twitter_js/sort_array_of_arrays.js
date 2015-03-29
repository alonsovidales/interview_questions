function Comparator(a,b){
        if (a[1] < b[1]) return -1;
        if (a[1] > b[1]) return 1;
        return 0;
}

var myArray = [
    [1, 'alfred', '...'],
    [23, 'berta', '...'],
    [2, 'zimmermann', '...'],
    [4, 'albert', '...'],
];

print(myArray.sort(Comparator));
