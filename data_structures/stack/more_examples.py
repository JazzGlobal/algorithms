from stack import Stack

def load_bullet(bullet, clip):
    clip.push(bullet)

def shoot_bullet(clip):
    bullet = clip.pop()
    print('BANG: You shot a ', bullet)


clipStack = Stack()
load_bullet('Regular Bullet', clipStack)
load_bullet('Poison Bullet', clipStack)
load_bullet('Regular Bullet', clipStack)

shoot_bullet(clipStack)
shoot_bullet(clipStack)
shoot_bullet(clipStack)

# Will print: 
# BANG You shot a Regular Bullet
# BANG You shot a Poison Bullet
# BANG You shot a Regular Bullet
