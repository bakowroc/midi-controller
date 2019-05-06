const navigator = require('jzz');
const player = require('play-sound')(opts = {player: "mplayer"});


function MIDIController() {
  const onNote = (message) => {
    const state = message.data[0] === 144;
    const note = message.data[1];
    const velocity = (message.data.length > 2) ? message.data[2] : 0;

    console.log(state, note, velocity);
    player.play("./C.wav", (err) => {
      if (err) console.log(err);
    });
  };

  const onFailure = () => {
    console.log('success')
  };

  const  onSuccess = (access) => {
    console.log(access.inputs.values());

    for (let input of access.inputs.values())
      input.onmidimessage = onNote;
  };

  navigator.requestMIDIAccess().then(onSuccess, onFailure)
}



MIDIController();
