from plotting import plot

# S = {2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}

S = {complex(1, -2), complex(2, -3)}

# plot(S, 4)

print({1j * z for z in S})
# plot({1j * z for z in S}, 4)