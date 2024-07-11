import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# The function below is the fade function
# It takes in a value t and returns the fade of t
# The fade function is used to smooth the curve
def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)

# The function below is the linear interpolation function
# It takes in a value t, and two values a and b
# It returns the linear interpolation of a and b based on t
def lerp(t, a, b):
    return a + t * (b - a)

# The function below is the gradient function
# It takes in a hash value, and two values x and y
# It returns the gradient of the hash value
# The gradient is calculated based on the hash value
def grad(hash, x, y):
    h = hash & 3
    u = np.where(h & 1 == 0, x, -x)
    v = np.where(h & 2 == 0, y, -y)
    return u + v

# The function below is the perlin noise function
# It takes in two values x and y, and an optional seed value
# It returns the perlin noise value based on the input values
# The perlin noise is calculated using the fade, lerp, and grad functions
def perlin_noise(x, y, seed=0):
    np.random.seed(seed)
    permutation = np.arange(256, dtype=int)
    np.random.shuffle(permutation)
    p = np.stack([permutation, permutation]).flatten()
    
    xi = x.astype(int) & 255
    yi = y.astype(int) & 255
    xf = x - x.astype(int)
    yf = y - y.astype(int)
    
    u = fade(xf)
    v = fade(yf)
    
    n00 = grad(p[p[xi] + yi], xf, yf)
    n01 = grad(p[p[xi] + yi + 1], xf, yf - 1)
    n10 = grad(p[p[xi + 1] + yi], xf - 1, yf)
    n11 = grad(p[p[xi + 1] + yi + 1], xf - 1, yf - 1)
    
    x1 = lerp(u, n00, n10)
    x2 = lerp(u, n01, n11)
    
    return lerp(v, x1, x2)

# The function below is the generate terrain function
# It takes in an optional seed, size, and scale value
# It returns the generated terrain based on the input values
# The terrain is generated using the perlin noise function
def generate_terrain(seed=0, size=256, scale=100.0):
    lin = np.linspace(0, 5, size, endpoint=False)
    x, y = np.meshgrid(lin, lin)
    noise = perlin_noise(x * scale, y * scale, seed=seed)
    terrain = (noise - noise.min()) / (noise.max() - noise.min())
    
    return terrain



# The function below is the plot heatmap function
# It takes in a terrain array and plots the heatmap
def plot_heatmap(terrain):
    plt.imshow(terrain, cmap='terrain')
    plt.colorbar()
    plt.title('Terrain Heatmap')
    plt.show()

# The function below is the plot 3D function
# It takes in a terrain array and plots the 3D plot
def plot_3d(terrain):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y = np.meshgrid(range(terrain.shape[0]), range(terrain.shape[1]))
    ax.plot_surface(x, y, terrain, cmap='terrain')
    plt.title('3D Terrain Map')
    plt.show()

# Generate terrain with specific seed and size
terrain = generate_terrain(seed=0, size=256, scale=100.0)

# Plot the terrain using both heatmap and 3D plot
plot_heatmap(terrain)
plot_3d(terrain)
