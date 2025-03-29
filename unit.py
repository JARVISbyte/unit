import sys


class BaseUnit:
    def __init__(self, t, l, m, i, T, n, L):
        self.t = t
        self.l = l
        self.m = m
        self.i = i
        self.T = T
        self.n = n
        self.L = L
        
    def __repr__(self):
        string = ""
        
        if self.t:
            string += 's'
            if self.t != 1:
                string += str(self.t)
            string += " "
        if self.l:
            string += 'm'
            if self.l != 1:
                string += str(self.l)
            string += " "
        if self.m:
            string += 'kg'
            if self.m != 1:
                string += str(self.m)
            string += " "
        if self.i:
            string += 'A'
            if self.i != 1:
                string += str(self.i)
            string += " "
        if self.T:
            string += 'K'
            if self.T != 1:
                string += str(self.T)
            string += " "
        if self.n:
            string += 'mol'
            if self.n != 1:
                string += str(self.n)
            string += " "
        if self.L:
            string += 'cd'
            if self.L != 1:
                string += str(self.L)
        
        return string.strip()
    
    def __mul__(self, other: 'BaseUnit'):
        return BaseUnit(self.t + other.t, self.l + other.l, self.m + other.m, self.i + other.i, self.T + other.T, self.n + other.n, self.L + other.L)
    
    def __truediv__(self, other: 'BaseUnit'):
        return BaseUnit(self.t - other.t, self.l - other.l, self.m - other.m, self.i - other.i, self.T - other.T, self.n - other.n, self.L - other.L)
    
    def __eq__(self, other: 'BaseUnit'):
        return (self.t == other.t) and (self.l == other.l) and (self.m == other.m) and (self.i == other.i) and (self.T == other.T) and (self.n == other.n) and (self.L == other.L)
    
    def __pow__(self, power):
        return BaseUnit(self.t*power, self.l*power, self.m*power, self.i*power, self.T*power, self.n*power, self.L*power)


Second    = BaseUnit(1, 0, 0, 0, 0, 0, 0)
Metre     = BaseUnit(0, 1, 0, 0, 0, 0, 0)
Kilogram  = BaseUnit(0, 0, 1, 0, 0, 0, 0)
Ampere    = BaseUnit(0, 0, 0, 1, 0, 0, 0)
Kelvin    = BaseUnit(0, 0, 0, 0, 1, 0, 0)
Mole      = BaseUnit(0, 0, 0, 0, 0, 1, 0)
Candela   = BaseUnit(0, 0, 0, 0, 0, 0, 1)


class Unit:
    def __init__(self, base_unit: BaseUnit, si_value: float = 1, name: str = ''):
        self.base_unit = base_unit
        self.si_value = si_value
        self.name = name
    
    def __repr__(self):
        return self.name if self.name else str(self.si_value) + ' ' + str(self.base_unit)

    def __add__(self, other: 'Unit'):
        return (self.base_unit == other.base_unit)
    
    def __eq__(self, other: 'Unit'):
        return self.__add__(other) and (self.si_value == other.si_value)
    
    def __mul__(self, other):
        if type(other) == type(self):
            return Unit(self.base_unit * other.base_unit, self.si_value * other.si_value)
        elif type(other) in (int, float):
            return Unit(self.base_unit, self.si_value * other)
        else:
            raise TypeError(f'Unit can only be multiplied by other unit or by int/float. Tried to multiply by {type(other)}.')
    
    def __pow__(self, power):
        return Unit(self.base_unit**power, self.si_value**power, ((f'({self.name})' if len(self.name)>1 else f'{self.name}') + f'{power}') if self.name else '')


# -- Length
u_m    = Unit(Metre, 1, 'm')
u_ft   = Unit(Metre, 0.30480, 'ft')
u_cm   = Unit(Metre, 0.01, 'cm')
u_mm   = Unit(Metre, 0.001, 'mm')
u_km   = Unit(Metre, 1000, 'km')
u_yd   = Unit(Metre, 0.9144, 'yd')
u_in   = Unit(Metre, 0.0254, 'in')
u_mile = Unit(Metre, 1609.344, 'mile')
u_nm   = Unit(Metre, 1852, 'nm')
u_au   = Unit(Metre, 149597870700, 'au')
u_pc   = Unit(Metre, 30856775814913673, 'pc')
u_ly   = Unit(Metre, 9460730472580800, 'ly')

# -- Area
u_m2    = u_m**2
u_ft2   = u_ft**2
u_cm2   = u_cm**2
u_mm2   = u_mm**2
u_km2   = u_km**2
u_yd2   = u_yd**2
u_in2   = u_in**2
u_mile2 = u_mile**2
u_nm2   = u_nm**2
u_au2   = u_au**2
u_pc2   = u_pc**2
u_ly2   = u_ly**2

# -- Volume
u_m3    = u_m**3
u_ft3   = u_ft**3
u_cm3   = u_cm**3
u_mm3   = u_mm**3
u_km3   = u_km**3
u_yd3   = u_yd**3
u_in3   = u_in**3
u_mile3 = u_mile**3
u_nm3   = u_nm**3
u_au3   = u_au**3
u_pc3   = u_pc**3
u_ly3   = u_ly**3

# -- Time
u_s     = Unit(Second, 1, 's')
u_ms    = Unit(Second, 0.001, 'ms')
u_us    = Unit(Second, 0.000001, 'us')
u_ns    = Unit(Second, 1e-9, 'ns')
u_min   = Unit(Second, 60, 'min')
u_h     = Unit(Second, 3600, 'h')
u_d     = Unit(Second, u_h.si_value * 24, 'd')
u_sd    = Unit(Second, 86164.0905, 'sd')
u_week  = Unit(Second, u_d.si_value * 7, 'week')
u_month = Unit(Second, u_d.si_value * 30, 'month')
u_y     = Unit(Second, u_d.si_value * 365, 'y')
u_ty    = Unit(Second, u_d.si_value * 365.24219, 'ty')

# -- Mass
u_kg   = Unit(Kilogram, 1, 'kg')
u_g    = Unit(Kilogram, 0.001, 'g')
u_t    = Unit(Kilogram, 1000, 't')
u_lb   = Unit(Kilogram, 0.45359237, 'lb')
u_un   = Unit(Kilogram, u_lb.si_value / 16, 'un')
u_slug = Unit(Kilogram, 14.59390, 'slug')

# -- Force
u_N   = Unit(Kilogram*Metre/Second**2, 1, 'N')
u_kN  = Unit(u_N.base_unit, 1000, 'kN')
u_MN  = Unit(u_N.base_unit, 1000000, 'MN')
u_GN  = Unit(u_N.base_unit, 1000000000, 'GN')
u_lbf = Unit(u_N.base_unit, 4.4482216152605, 'lbf')

# -- Velocity
u_ms  = Unit(Metre/Second, 1, 'm/s')
u_kph = Unit(Metre/Second, u_km.si_value/u_h.si_value, 'km/h')
u_mph = Unit(Metre/Second, 0.44704, 'mph')
u_kt  = Unit(Metre/Second, u_nm.si_value/u_h.si_value, 'kt')
u_kn  = Unit(Metre/Second, u_nm.si_value/u_h.si_value, 'kn')
u_ks  = Unit(Metre/Second, 1000, 'km/s')
u_c   = Unit(Metre/Second, 299792458, 'c')

# -- Pressure
u_Pa  = Unit(u_N.base_unit/Metre**2, 1, 'Pa')
u_kPa = Unit(u_Pa.base_unit, 1000, 'kPa')
u_MPa = Unit(u_Pa.base_unit, 1000000, 'MPa')
u_GPa = Unit(u_Pa.base_unit, 1000000000, 'GPa')
u_Atm = Unit(u_Pa.base_unit, 101325, 'atm')
u_bar = Unit(u_Pa.base_unit, 100000, 'bar')
u_psi = Unit(u_Pa.base_unit, u_lbf.si_value/u_in2.si_value, 'psi')

# -- Power
u_W  = Unit(u_N.base_unit*Metre/Second, 1, 'W')
u_mW = Unit(u_W.base_unit, 0.001, 'mW')
u_kW = Unit(u_W.base_unit, 1000, 'kW')
u_MW = Unit(u_W.base_unit, 1000000, 'MW')
u_hp = Unit(u_W.base_unit, 550 * u_lbf.si_value * u_ft.si_value / u_s.si_value, 'hp')
u_nuclear = Unit(u_W.base_unit, 1000000000, 'Nuclear')

units = (
    u_m , u_ft , u_cm , u_mm , u_km , u_yd , u_in , u_mile , u_nm , u_au , u_pc , u_ly ,
    u_m2, u_ft2, u_cm2, u_mm2, u_km2, u_yd2, u_in2, u_mile2, u_nm2, u_au2, u_pc2, u_ly2,
    u_m3, u_ft3, u_cm3, u_mm3, u_km3, u_yd3, u_in3, u_mile3, u_nm3, u_au3, u_pc3, u_ly3,
    u_s, u_ms, u_us, u_ns, u_min, u_h, u_d, u_sd, u_week, u_month, u_y, u_ty,
    u_kg, u_g, u_t, u_lb, u_un, u_slug,
    u_N, u_kN, u_MN, u_GN, u_lbf,
    u_ms, u_kph, u_mph, u_kt, u_kn, u_ks, u_c,
    u_Pa, u_kPa, u_MPa, u_GPa, u_Atm, u_bar, u_psi,
    u_W, u_mW, u_kW, u_MW, u_hp, u_nuclear,
)

varunits = """u_m , u_ft , u_cm , u_mm , u_km , u_yd , u_in , u_mile , u_nm , u_au , u_pc , u_ly ,
u_m2, u_ft2, u_cm2, u_mm2, u_km2, u_yd2, u_in2, u_mile2, u_nm2, u_au2, u_pc2, u_ly2,
u_m3, u_ft3, u_cm3, u_mm3, u_km3, u_yd3, u_in3, u_mile3, u_nm3, u_au3, u_pc3, u_ly3,
u_s, u_ms, u_us, u_ns, u_min, u_h, u_d, u_sd, u_week, u_month, u_y, u_ty,
u_kg, u_g, u_t, u_lb, u_un, u_slug,
u_N, u_kN, u_MN, u_GN, u_lbf,
u_ms, u_kph, u_mph, u_kt, u_kn, u_ks, u_c,
u_Pa, u_kPa, u_MPa, u_GPa, u_Atm, u_bar, u_psi,
u_W, u_mW, u_kW, u_MW, u_hp, u_nuclear,"""

class Quantity:
    def __init__(self, unit: Unit, value: float):
        self.unit = unit
        self.value = value
    
    def __repr__(self):
        return str(self.value) + ' (' + str(self.unit) + ')'
    
    def __add__(self, other: 'Quantity'):
        if not (self.unit + other.unit):
            raise Exception('Cannot add units with different bases')
        
        return Quantity(self.unit, self.value + other.value*other.unit.si_value/self.unit.si_value)
    
    def __neg__(self):
        return Quantity(self.unit, -self.value)
    
    def __sub__(self, other):
        return self.__add__(other.__neg__())
    
    def __mul__(self, other):
        return Quantity(self.unit * other.unit, self.value * other.value)
    
    def __pow__(self, power):
        return Quantity(self.unit**power, self.value**power)
    
    def to_si(self):
        return Quantity(Unit(self.unit.base_unit), self.unit.si_value * self.value)
    
    def in_si(self):
        return self.unit.si_value * self.value

'''
v1 = Quantity(u_ms, 12)
v2 = Quantity(u_mph, 12)

print(v1)
print(v2)
print(str(v1 - v2))


l1 = Quantity(u_m, 1)
l2 = Quantity(u_ft, 1)

print(l1*l2)

l3 = l2**4
print(l3.unit.base_unit)
print(l3.to_si().unit.base_unit)
'''

if __name__ == '__main__':
    argv = sys.argv

    if len(argv) == 2:
        if argv[1] == 'help':
            print("unit is a small utility created to allow arithmetic operations without worrying about physical units.")
            print()
            print("Syntax")
            print("\t help - prints this page")
            print("\t <unit_name> - prints information about the unit, in the form \n\t\t <name> (<dimensioning>) <SI value>")
            print("\t list - lists all default units")
            print("\t varlist - lists all default units' variable names")
            print("\t <unit_name> -> <unit_name> - converts first unit to second")
            print("\t <unit_name> to <unit_name> - converts first unit to second")
            print("\t <amount> <unit_name> -> <unit_name> - converts given quantity of the first unit to the second unit")
            print("\t <amount> <unit_name> to <unit_name> - converts given quantity of the first unit to the second unit")
        elif argv[1] == 'list':
            print(units)
        elif argv[1] == 'varlist':
            print(varunits)
        else:
            flag = False
            for unit in units:
                if argv[1] == unit.name:
                    print(f"{unit.name} ({unit.base_unit}) {unit.si_value}")
                    flag = True
            if not flag:
                print(f'No unit with name {argv[1]} found')
    
    elif len(argv) == 4:
        if argv[2] in ('->', 'to'):
            ufrom = None
            uto = None
            for unit in units:
                if argv[1] == unit.name:
                    ufrom = unit
                if argv[3] == unit.name:
                    uto = unit

            if ufrom and uto:
                print(f'1 ({ufrom}) =', Quantity(uto, 0) + Quantity(ufrom, 1))
    
    elif len(argv) == 5:
        if argv[3] in ('->', 'to'):
            ufrom = None
            uto = None
            value = float(argv[1])

            for unit in units:
                if argv[2] == unit.name:
                    ufrom = unit
                if argv[4] == unit.name:
                    uto = unit

            if ufrom and uto:
                print(f'{value} ({ufrom}) =', Quantity(uto, 0) + Quantity(ufrom, value))
    