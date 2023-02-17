# this code was written by chatGPT
import random

# Define the parameters of the genetic algorithm
POPULATION_SIZE = 100
GENE_LENGTH = 10
MUTATION_RATE = 0.1

# Define the fitness function that the algorithm will try to optimize
def fitness_function(gene):
    # In this example, the fitness function simply counts the number of 1s in the gene
    return sum(gene)

# Define the functions for creating and mutating genes
def create_gene():
    return [random.randint(0, 1) for _ in range(GENE_LENGTH)]

def mutate_gene(gene):
    for i in range(GENE_LENGTH):
        if random.random() < MUTATION_RATE:
            gene[i] = 1 - gene[i]

# Define the main genetic algorithm function
def genetic_algorithm():
    # Initialize the population with random genes
    population = [create_gene() for _ in range(POPULATION_SIZE)]

    # Iterate through generations
    for generation in range(100):
        # Evaluate the fitness of each gene
        fitness_values = [fitness_function(gene) for gene in population]

        # Select the best genes for reproduction
        selected_indices = sorted(range(POPULATION_SIZE), key=lambda i: fitness_values[i], reverse=True)[:int(POPULATION_SIZE/2)]
        selected_genes = [population[i] for i in selected_indices]

        # Create new genes through crossover and mutation
        new_population = []
        for i in range(POPULATION_SIZE):
            parent1 = random.choice(selected_genes)
            parent2 = random.choice(selected_genes)
            child = [parent1[j] if random.random() < 0.5 else parent2[j] for j in range(GENE_LENGTH)]
            mutate_gene(child)
            new_population.append(child)

        population = new_population

    # Return the best gene found
    best_index = max(range(POPULATION_SIZE), key=lambda i: fitness_values[i])
    return population[best_index]

# Run the genetic algorithm and print the best gene found
best_gene = genetic_algorithm()
print("Best gene found:", best_gene)
