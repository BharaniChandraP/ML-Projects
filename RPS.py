import random

def player(prev_play, opponent_history=[], state={}):
    """
    This player function uses a persistent 'state' dictionary
    to store a predictive model (Markov chain).
    
    The 'state' dictionary holds:
    - 'model': A dictionary where keys are move sequences (e.g., "RPS")
               and values are dictionaries of move counts (e.g., {'R': 1, 'P': 5}).
    - 'history': A list of the opponent's moves for the current match.
    - 'k': The length of the move sequence to use as a key.
    """
    
    ideal_response = {'R': 'P', 'P': 'S', 'S': 'R'}
    moves = ['R', 'P', 'S']
    
    # --- 1. Handle Match Reset ---
    # If prev_play is empty, it's the start of a new match.
    # Reset the history and model.
    if prev_play == "":
        state['history'] = []
        state['model'] = {}
        state['k'] = 4  # We will look for patterns of 4 moves
        
        # Clear the opponent_history list as well, just in case
        opponent_history.clear() 
        
        # Make a random first move
        my_move = random.choice(moves)
        opponent_history.append(my_move) # Save our move
        return my_move

    # --- 2. Update Model (Learn from Opponent) ---
    # Add the opponent's last move to our history
    state['history'].append(prev_play)
    
    k = state['k']
    history = state['history']
    
    # If we have enough history, update the model
    # We learn what move (prev_play) followed a sequence (key)
    if len(history) > k:
        # The sequence of moves *before* the opponent's last play
        key = "".join(history[-(k+1):-1])
        
        # The move that followed that sequence
        result = prev_play 
        
        # Initialize the key in the model if it's new
        if key not in state['model']:
            state['model'][key] = {'R': 0, 'P': 0, 'S': 0}
            
        # Increment the count for the move that followed
        state['model'][key][result] += 1

    # --- 3. Make Prediction ---
    my_move = random.choice(moves) # Default to random if no pattern
    
    # If we have enough history to make a prediction
    if len(history) >= k:
        # The *current* last sequence
        current_key = "".join(history[-k:])
        
        # Check if we have data for this sequence
        if current_key in state['model']:
            # Get the move counts for this sequence
            predictions = state['model'][current_key]
            
            # Find the move the opponent is *most likely* to play
            if max(predictions.values()) > 0:
                predicted_move = max(predictions, key=predictions.get)
            
                # Play the move that *beats* the prediction
                my_move = ideal_response[predicted_move]
            
    # --- 4. Return Our Move ---
    # We must save our *own* move to the provided list
    # to maintain state for the next call (this is a hack
    # required by the project's design, but this solution 
    # uses the 'state' dict instead. We still need to pass 
    # something to opponent_history to keep it non-empty).
    opponent_history.append(my_move)
    return my_move
