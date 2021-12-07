console.log("hello")
let socketURL = "ws://" + window.location.host + "/ws/positions/"
const socket = new WebSocket(socketURL)
console.log(socket)
socket.onmessage = (e) =>{
    let positions_data = JSON.parse(e.data)
    $('#positions-table').empty()
    for (index in positions_data['positions']){
        let crypto = positions_data['positions'][index]
        console.log(crypto)
        $('#positions-table').append(
            `
            <tr>
            <td><img src="${crypto.image}" alt="crpto-image" height="70"></td>
            <td class="align-middle">${crypto.name}</td>
            <td class="align-middle">${crypto.rank}</td>
            <td class="align-middle">${crypto.market_cap}</td>
            <td class="align-middle">${crypto.price}</td>
            </tr>
            `
            )
    }

}