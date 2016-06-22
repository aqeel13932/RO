/**
 * Created by t420s on 14.03.2016.
 */
document.addEventListener('keydown', function(event) {
    switch (event.keyCode) {
        case 37:
            sendData('left');
            break;
        case 38:
            sendData('up');
            break;
        case 39:
            sendData('right');
            break;
        case 40:
            sendData('down');
            break;
    }
});

function sendData(key) {
    $("#button").text(key);
    $.ajax({
        url: '/move',
        type: 'POST',
        data: {
            button: key
        },
        success: function(response){
            console.log('success:' + response)
        },
        error: function(error){
            console.error(error)
        }
    });
}

