class MiRange:
    def __init__(this,num_max):
        this.num_max = num_max;
        this.num_actual = 0;

    def __iter__(this):
        return this;

    def __next__(this):
        if this.num_actual < this.num_max:
            n = this.num_actual;
            this.num_actual += 1;
            return n;
        else:
            raise StopIteration();
        
print(list(MiRange(10)));
