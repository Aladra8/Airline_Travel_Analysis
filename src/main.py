from data_preprocessing import load_data, clean_and_preprocess_data
from graph_algorithms import create_graph, calculate_network_metrics
from network_analysis import analyze_travel_time_thresholds
from visualization import visualize_networks

# Load and preprocess data
meta_data = load_data()
cleaned_data = clean_and_preprocess_data(meta_data)

# Create the graph
graph = create_graph(cleaned_data, reachability_data)  # You need to define `reachability_data`

# Calculate network metrics
degree_centrality, betweenness_centrality, pagerank, clustering_coefficient = calculate_network_metrics(graph)

# Analyze travel time thresholds
threshold_values = [0.1, 0.2, 0.3]
results_thresholds = analyze_travel_time_thresholds(graph, threshold_values)

# Visualize networks
visualize_networks(graph_us, graph_canada)  # You need to define `graph_us` and `graph_canada`
