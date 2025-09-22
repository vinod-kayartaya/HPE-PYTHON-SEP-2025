fields = 'name,email,phone,city'.split(',')
vals = 'Vinod Kumar,vinod@vinod.co,9731424784,Bangalore'.split(',')

print(f'{fields = }')
print(f'{vals = }')

z = zip(fields, vals)
# z = [('id', '1121'), ('name','Vinod Kumar'), ('email', 'vinod@vinod.co'), (....), (....)]
print(f'{list(z) = }')

p1 = dict(zip(fields, vals))
print(f'{p1 = }')