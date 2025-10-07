$(document).ready(function() {
    const totalPlayersInput = $('#total_players');
    const startBtn = $('#start_btn');
    const nextBtn = $('#next_btn');
    const playerNumberDisplay = $('#player_number');
    const progressTracker = $('#progress');

    startBtn.on('click', function() {
        const totalPlayers = totalPlayersInput.val();
        if (totalPlayers < 1) {
            alert("Please enter a number greater than 0.");
            return;
        }
        
        $.post('/start', { total_players: totalPlayers })
            .done(function(response) {
                if (response.success) {
                    totalPlayersInput.prop('disabled', true);
                    startBtn.hide();
                    nextBtn.show();
                    playerNumberDisplay.text("--");
                    progressTracker.text("[0/" + totalPlayers + "]");
                }
            })
            .fail(function(jqXHR) {
                alert(jqXHR.responseJSON.error);
            });
    });

    nextBtn.on('click', function() {
        $.post('/next_player')
            .done(function(response) {
                playerNumberDisplay.text(response.number);
                progressTracker.text(response.progress);
                if (response.is_last) {
                    nextBtn.prop('disabled', true);
                    nextBtn.text("Auction Complete");
                    /* alert("All players have been called!"); */
                }
            });
    });
});
