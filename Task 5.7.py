#1. We got 5 on display, because mod_c.x variable has been imported from mod_b.py
#2. If we change x from 5 to [1, 2, 3] in mod_c.py nothing changes. We still don't use x from mod_c.py.
#But if we change x in mod_b.py we get [1, 2, 3] on display, because mod_b.py overrides mod_c.x
#3. If we change import description in mod_a we still can use mod_c.x and get [1, 2, 3] on display
# But now we can use x without prefix and get 5, because mod_c.py was imported first and we got x from there