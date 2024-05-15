let letters = [];
let routes = [];
let routeIndex = -1;

fetch('./board.txt')
    .then(response => response.text())
    .then(data => {
        letters = data.split("");
        let table = document.getElementById("grid");

        let i = 0;
        for (let row = 0; row < 4; row++) {
            let tr = document.createElement("tr");
            for (let col = 0; col < 4; col++) {
                let td = document.createElement("td");
                let txt = document.createTextNode(letters[i]);
                td.appendChild(txt);
                tr.appendChild(td);
                i++;
            }
            table.appendChild(tr);
        }
    })
    .catch(error => console.error('Error:', error));

fetch('http://localhost:5000/get_paths')
    .then(response => response.json())
    .then(data => {
        routes = Object.keys(data)
            .map(word => ({ word, route: data[word] }))
            // Sort words in descending order of their length
            .sort((a, b) => b.word.length - a.word.length);
    })
    .catch(error => console.error('Error:', error));
// ...
document.getElementById('nextButton').addEventListener('click', function nextButtonClicked() {
    let svg = document.getElementById('svgRoot');
    let offsetTop = document.getElementById('word').offsetTop;
    let tableCell = document.querySelector("#grid td");
    let svgX = tableCell.getBoundingClientRect().width / 2;
    let svgY = tableCell.getBoundingClientRect().height / 2;
    svg.innerHTML = '';

    if(++routeIndex >= routes.length) {
        routeIndex = 0;
    }

    let route = routes[routeIndex];
    document.getElementById('word').innerText = route.word;
    for(let i = 0; i < route.route.length - 1; i++) {
        let [c1X, c1Y] = route.route[i];
        let [c2X, c2Y] = route.route[i + 1];

        let p1X = c1Y * tableCell.getBoundingClientRect().width + svgX;
        let p1Y = c1X * tableCell.getBoundingClientRect().height + svgY + offsetTop;
        let p2X = c2Y * tableCell.getBoundingClientRect().width + svgX;
        let p2Y = c2X * tableCell.getBoundingClientRect().height + svgY + offsetTop;

        // Starting circle (Green)
        if (i == 0) {
            let circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            circle.setAttribute('cx', p1X.toString());
            circle.setAttribute('cy', p1Y.toString());
            circle.setAttribute('r', '10');
            circle.style.fill = 'green';

            svg.appendChild(circle);
        }

        let line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line.setAttribute('x1', p1X.toString());
        line.setAttribute('y1', p1Y.toString());
        line.setAttribute('x2', p2X.toString());
        line.setAttribute('y2', p2Y.toString());
        line.style.stroke = 'black';
        line.style.strokeWidth = '2px';

        svg.appendChild(line);
        
        // Ending circle (Red)
        if (i == route.route.length - 2) {
            let circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            circle.setAttribute('cx', p2X.toString());
            circle.setAttribute('cy', p2Y.toString());
            circle.setAttribute('r', '10');
            circle.style.fill = 'red';

            svg.appendChild(circle);
        }
    }
});