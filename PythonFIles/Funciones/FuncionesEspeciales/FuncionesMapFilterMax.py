
#funcion map
numeros = [47,345,2,34,45,55,123,12];

newList = list(map(lambda x: x*2 +3,numeros)); #multiplicar por dos y sumarle 3
print(newList);

#diccionario
aquarium_creatures = [
	{"name": "sammy", "species": "shark", "tank number": 11, "type": "fish"},
	{"name": "ashley", "species": "crab", "tank number": 25, "type": "shellfish"},
	{"name": "jo", "species": "guppy", "tank number": 18, "type": "fish"},
	{"name": "jackie", "species": "lobster", "tank number": 21, "type": "shellfish"},
	{"name": "charlie", "species": "clownfish", "tank number": 12, "type": "fish"},
	{"name": "olly", "species": "green turtle", "tank number": 34, "type": "turtle"}
]

def new_tank_number(aquarium_creatures,new_tank_number):
    def apply(x):
        x["tank number"] = new_tank_number;
        return x;
    return list(map(apply,aquarium_creatures));

lista= new_tank_number(aquarium_creatures,10);
print(lista);

numbers = [2,4,6,8,10,12,14,16,18,20];
powers = [1,2,3,4,5];
lista = (list(map(pow,numbers,powers)));
print(lista);

#funcion filter
lista = list(filter(lambda x: x%5 == 0, range(0,100)));
print(lista);

print(list(filter(lambda x: 'e' in x.lower(), ['levi','leon','cristiano','ronaldo'])));

creature_names = ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie'];
lista = list(filter(lambda x:x[0].lower() in 'aeiou', creature_names));
print(lista);

def creatureNames(x):
	return x[0].lower() in 'aeiou';

lista2 = list(filter(creatureNames,creature_names));
print(lista2);

aquarium_tanks = [11, False, 18, 21, "", 12, 34, 0, [], {}];
lista3 = list(filter(None,aquarium_tanks));
print(lista3);

#filtrar un diccionario
def filter_Set(aquarium_creatures,searchString):
	def iterador(x):
		for v in x.values():
			if(searchString in v):
				return True;
			return False;
	return filter(iterador,aquarium_creatures);

filteres_records = filter_Set(aquarium_creatures,"");
print(list(filteres_records));