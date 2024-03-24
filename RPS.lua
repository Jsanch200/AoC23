local rock = 1 
local paper = 2 
local sissors = 3

local function get_result(opponent)
    local opponent = math.random (1, 3)
    io.write ("RPS Game! Choose one: Rock | Paper | Sissors: ")
    local player = io.read():lower()
   
    if opponent == 1 then
        print("CPU chose rock")
    elseif opponent == 2 then
        print("CPU chose paper")
    elseif opponent == 3 then
        print("CPU chose sissors")
    end
    if player == "rock" then
        if opponent == rock then
            print ("Tie!")
        elseif opponent == paper then
            print ("You lose!")
        elseif opponent == sissors then
            print ("You win!")
        end
    elseif player == "paper" then
        if opponent == rock then
            print ("You win!")
        elseif opponent == paper then
            print ("Tie!")
        elseif opponent == sissors then
            print ("You lose!")
        end
    elseif player == "sissors" then
        if opponent == rock then
            print ("You lose!")
        elseif opponent == paper then
            print ("You win!")
        elseif opponent == sissors then
            print ("Tie!")
        end
    end
end

get_result()