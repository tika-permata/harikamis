const data = [
    {
        name: "udin",
        age: 10
    },
    {
        name: "ujang",
        age: 11
    },
    {
        name: "asep",
        age: 12
    }
];

function printData(data) {
    data.forEach(item => {
        console.log(`Name: ${item.name}, Age: ${item.age}`);
    });
}

printData(data);
