def cakes(eggs, butter, flour):
    egg_count = eggs // 5
    butter_count = butter // 250
    flour_count = flour // 250
    return min(egg_count,butter_count,flour_count)