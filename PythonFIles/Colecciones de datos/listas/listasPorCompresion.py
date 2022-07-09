lis = [x*2 for x in[2,3,4,5]];
print(lis);

p = 'Python'
lis2 = [ord(x) for x in p];
print(lis2);

lis3 = [x+5 if x>4 else x -10 for x in range(10)];
print(lis3);

lis4 = ['Python'[:i] for i in range(7)];
print(lis4);

x = ['Perro','Gato','Elefante','girafa','reno','oso'];
y = [2,3,1,54,21,23];
lis5 = [xs for xs ,ys in zip(x,y) if 'e' in xs and ys >0];
print(lis5);