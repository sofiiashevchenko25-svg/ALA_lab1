import numpy as np
import matplotlib.pyplot as plt

# =========================
# PART 1 — 2D TRANSFORMATIONS
# =========================
object = np.array([
    [-1, -1],
    [1, -1],
    [0.5, 0],
    [1.2, 1],
    [0, 0.5],
    [-0.8, 1.5],
    [-1, 0],
    [-1, -1]
])
plt.plot(object[:, 0], object[:, 1])
plt.axis('equal')
plt.show()

def stretch(X, a, b):
    X_copy = X.copy()
    Mat = np.array([[a, 0], [0, b]])
    result = Mat @ X_copy.T
    return result.T, Mat

show = stretch(object, 2, 5)[0]
print(stretch(object, 2, 5)[1])
plt.plot(show[:, 0], show[:,1 ])
plt.axis('equal')
plt.show()

show = stretch(object, 5, 2)[0]
print(stretch(object, 5, 2)[1])
plt.plot(show[:, 0], show[:,1 ])
plt.axis('equal')
plt.show()


def shear(X, a, b):
    X_copy = X.copy()
    Mat = np.array([[1, a], [b, 1]])
    result = Mat @ X_copy.T
    return result.T, Mat

show = shear(object, 0, 0.5)[0]
print(shear(object, 0, 0.5)[1])
plt.plot(show[:, 0], show[:,1 ])
plt.axis('equal')
plt.show()

show = shear(object, 0.5, 0)[0]
print(shear(object, 0.5, 0)[1])
plt.plot(show[:, 0], show[:,1 ])
plt.axis('equal')
plt.show()


def reflection(X, a, b):
    X_copy = X.copy()
    d = 1/((a**2) + (b**2))
    Mat = d*np.array([[(a**2) - (b**2), 2*a*b], [2*a*b, (b**2) - (a**2)]])
    result = Mat @ X_copy.T
    return result.T, Mat

show = reflection(object, 2, 5)[0]
print(reflection(object, 2, 5)[1])
plt.plot(show[:, 0], show[:,1 ])
plt.axis('equal')
plt.show()

show = reflection(object, 5, 2)[0]
print(reflection(object, 5, 2)[1])
plt.plot(show[:, 0], show[:,1 ])
plt.axis('equal')
plt.show()

def rotation(X, θ):
    X_copy = X.copy()
    Mat = np.array([[np.cos(θ), -np.sin(θ)], [np.sin(θ), np.cos(θ)]])
    result = Mat @ X_copy.T
    return result.T, Mat

show = rotation(object, np.pi / 4)[0]
print(rotation(object, np.pi / 4)[1])
plt.plot(show[:, 0], show[:,1 ])
plt.axis('equal')
plt.show()

show = rotation(object, np.pi)[0]
print(rotation(object, np.pi)[1])
plt.plot(show[:, 0], show[:,1 ])
plt.axis('equal')
plt.show()

#combination of transformation
show = stretch(rotation(shear(object, 0.6, 0.7)[0], np.pi/3)[0], 10, 21 )[0]
print(stretch(rotation(shear(object, 0.6, 0.7)[0], np.pi/3)[0], 10, 21 )[1])
plt.plot(show[:, 0], show[:,1 ])
plt.axis('equal')
plt.show()

show = shear(rotation(stretch(object, 10, 21)[0], np.pi/3)[0], 0.6, 0.7 )[0]
print(shear(rotation(stretch(object, 10, 21)[0], np.pi/3)[0], 0.6, 0.7 )[1])
plt.plot(show[:, 0], show[:,1 ])
plt.axis('equal')
plt.show()

show = rotation(shear(stretch(object, 10, 21)[0], 0.6, 0.7)[0], np.pi/3)[0]
print(rotation(shear(stretch(object, 10, 21)[0], 0.6, 0.7)[0], np.pi/3)[1])
plt.plot(show[:, 0], show[:,1 ])
plt.axis('equal')
plt.show()

# =========================
# PART 2 — 3D MODEL
# =========================

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


# Read OFF file
with open("piano_0247.off", "r") as file:
    lines = file.readlines()

n_vertices, n_faces, _ = map(int, lines[1].split())

vertices = []

for line in lines[2:2 + n_vertices]:
    x, y, z = map(float, line.split())
    vertices.append([x, y, z])

vertices = np.array(vertices)

faces = []

for line in lines[2 + n_vertices:2 + n_vertices + n_faces]:
    values = list(map(int, line.split()))
    faces.append(values[1:])

def plot_3d_model(vertices, faces):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    triangles = []

    for face in faces:
        triangles.append(vertices[face])

    mesh = Poly3DCollection(triangles, alpha=0.7)
    ax.add_collection3d(mesh)

    ax.set_xlim(vertices[:, 0].min(), vertices[:, 0].max())
    ax.set_ylim(vertices[:, 1].min(), vertices[:, 1].max())
    ax.set_zlim(vertices[:, 2].min(), vertices[:, 2].max())

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.show()

def rotate_xy (X, θ):
    X_copy = X.copy()
    Mat = np.array([[np.cos(θ), -np.sin(θ), 0], [np.sin(θ), np.cos(θ), 0], [0, 0, 1]])
    result = Mat @ X_copy.T
    return result.T, Mat

def rotate_yz (X, θ):
    X_copy = X.copy()
    Mat = np.array([[1, 0, 0], [0,  np.cos(θ), -np.sin(θ)], [0,  np.sin(θ), np.cos(θ)]])
    result = Mat @ X_copy.T
    return result.T, Mat

def rotate_xz (X, θ):
    X_copy = X.copy()
    Mat = np.array([[np.cos(θ),0, -np.sin(θ)], [0, 1, 0], [np.sin(θ), 0, np.cos(θ)]])
    result = Mat @ X_copy.T
    return result.T, Mat

plot_3d_model(vertices, faces)
show = rotate_xy(vertices, np.pi)
print(rotate_xy(vertices, np.pi)[1])
plot_3d_model(show[0], faces)

show = rotate_yz(vertices, np.pi/2)
print(rotate_yz(vertices, np.pi/2)[1])
plot_3d_model(show[0], faces)

show = rotate_xz(vertices, np.pi/4)
print(rotate_xz(vertices, np.pi/4)[1])
plot_3d_model(show[0], faces)

show = rotate_yz(
    rotate_xy(
        rotate_xz(vertices, 3*np.pi/2)[0],
        np.pi/3
    )[0],
    np.pi
)[0]

plot_3d_model(show, faces)
M = rotate_yz(vertices, np.pi)[1] @ rotate_xy(vertices, np.pi/3)[1] @ rotate_xz(vertices, 3*np.pi/2)[1]
print(M)
