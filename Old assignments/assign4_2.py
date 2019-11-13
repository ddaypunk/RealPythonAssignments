__author__ = 'Andy Delso'

def toFahrenheit(inCelsius):
    return (inCelsius*(9/5.0)+32)


def toCelsius(inFahrenheit):
    return ((inFahrenheit-32)*(5/9.0))

#if __name__ == 'main':
entryInCelsius = int(raw_input('What are the degrees in Celsius?: '))
entryInFahrenheit = int(raw_input('What are the degrees in Fahrenheit?: '))

print '\n' + str(entryInCelsius) + 'degrees C = ' + str(toFahrenheit(entryInCelsius)) + ' degrees F'
print str(entryInFahrenheit) + 'degrees F = ' + str(toCelsius(entryInFahrenheit)) + ' degrees C'
