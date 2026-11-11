import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# GRADIENT DESCENT TRAINING FUNCTION
# ==========================================
def train_linear_regression(X, y, initial_weights, learning_rate, max_iters=50000, delta_threshold=1e-5, divergence_threshold=1e9):
    """
    Trains a multi-variable linear regression model using Gradient Descent.
    Model: y^ = w[0] + w[1]*x1 + w[2]*x2
    """

    # Initialize weights and history trackers (for intermediate results and graphs)
    w = np.array(initial_weights, dtype=float)
    N = len(y) # Number of training samples
    history = []
    
    # Add a column of 1s to X for the bias term w[0]
    X_b = np.c_[np.ones((N, 1)), X]

    # Track previous sum of squared errors (SSE) to check for convergence
    prev_sse = float('inf')
    stop_reason = "Max Iterations Reached" # Default stop reason

    # Loop for Gradient Descent (Does entire batch at once)
    for iteration in range(max_iters):
        # Predictions: y^ = X_b * w
        # Applies weights to each record
        y_pred = X_b.dot(w)
        
        # Compute errors (Actual - Predicted) for each row
        errors = y - y_pred
        
        # Compute sum of squared errors (SSE) for batch
        sse = np.sum(errors ** 2)

        # Add current iteration SSE to history for plotting graphs later
        history.append((iteration, sse))
        
        # Check for divergence stopping condition (SSE > divergence_threshold or NaN)
        if np.isnan(sse) or sse > divergence_threshold or (iteration > 0 and (sse - prev_sse) > divergence_threshold):
            stop_reason = "Error Passed Divergence Threshold (Error Exploded)"
            break
            
        # Check for convergence stopping condition (Delta SSE < delta_threshold)
        if iteration > 0 and abs(prev_sse - sse) < delta_threshold:
            stop_reason = "Error Converged (Delta SSE < delta_threshold)"
            break
            
        # Compute the gradient for SSE loss: d(SSE)/dw = -2 * X_b.T dot errors
        gradient = -2.0 * X_b.T.dot(errors)
        
        # Update weights using gradient and learning rate
        w -= learning_rate * gradient
        prev_sse = sse

    final_sse = float('inf')

    # Final SSE is the last recorded SSE in history if history is not empty
    if history:
        final_sse = history[-1][1]  

    # Return final weights, SSE, stopping reason, and history of SSE for plotting
    return w, final_sse, stop_reason, history


if __name__ == "__main__":

    # ==========================================
    # LOAD DATASET AND DATA EXPLORATION
    # ==========================================

    # Load dataset into pandas DataFrame
    df = pd.read_csv("A4-data.csv")
    
    print("--- DATA EXPLORATION ---")
    print(df.head())
    print("\nSummary Statistics:")
    # Get min, max, mean, and std. dev for each column except ID (since all continuous)
    stats = df[['AGE', 'HEARTRATE', 'OXYCON']].describe().T[['min', 'max', 'mean', 'std']]
    print(stats)

    # Training data set with descriptive features only
    X = df[['AGE', 'HEARTRATE']].values

    # Target variable (OXYCON) values
    y = df['OXYCON'].values

    # Set pandas display format to show floats with 4 decimal places normally (no scientific notation) for displaying SSE
    pd.set_option('display.float_format', lambda x: '%.4f' % x)

    # ==========================================
    # TRAIN MODEL
    # ==========================================
    
    # Learning rates based on assignment specifications.
    learning_rates = [0.0002, 0.000002, 0.00000002]

    # Set a random seed so the random weights stay the same on every rerun
    np.random.seed(42)

    # Get 3 random starting weights between -10 and 10
    random_weights = np.round(np.random.uniform(low=-10.0, high=10.0, size=3), 2).tolist()
    
    init_weight_categories = [
        ("Zeros Initialization [0, 0, 0]", [0.0, 0.0, 0.0]),
        ("Specific Initialization [-59.5, -0.15, 0.60]", [-59.5, -0.15, 0.60]),
        (f"Random Initialization {random_weights}", random_weights)
    ]


    results_summary = []
    all_histories = {}

    # Track which run it is (for summary table)
    run_id = 1

    for cat_name, init_weights in init_weight_categories:
        for lr in learning_rates:
            final_w, final_sse, reason, history = train_linear_regression(X, y, init_weights, lr)
            
            results_summary.append({
                "Run": f"Run {run_id}",
                "Init Weights": init_weights,
                "Learning Rate": lr,
                "Stop Condition": reason,
                "Final w0": round(final_w[0], 4),
                "Final w1": round(final_w[1], 4),
                "Final w2": round(final_w[2], 4),
                "Final SSE": round(final_sse, 4)
            })


            # Store the history for plotting graphs later
            iters, sses = zip(*history)
            # Cap SSE values for clean rendering (incase they explode to infinity)
            sses_capped = [min(s, 1e8) for s in sses]

            all_histories[f"Run {run_id}"] = {
                "iters": iters,
                "sses_capped": sses_capped,
                "label": f"Run {run_id} (LR={lr})"
            }
            run_id += 1


    # ==========================================
    # PRESENTING INTERMEDIATE RESULTS
    # ==========================================
    print("\n" + "="*80)
    print("INTERMEDIATE TRAINING RESULTS (CHECKPOINT SNAPSHOTS)")
    print("="*80)

    for key, val in all_histories.items():
        print(f"\n{key} - {val['label']}")
        print("-"*80)

        total_iters = len(val['iters'])

        # Common iteration checkpoints to see intermediate results
        checkpoint_indices = [0, 1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 25000, total_iters - 1]
        # Get valid indices for run (if run terminated early)
        valid_indices = sorted(list(set([idx for idx in checkpoint_indices if idx < total_iters])))

        print(f"{'Iteration':<12} | {'Sum of Squared Errors (SSE)':<25}")
        print("-" * 42)
        
        for idx in valid_indices:
            iteration, sse = val['iters'][idx], val['sses_capped'][idx]
            print(f"{iteration:<12} | {sse:<25.4f}")

    # ==========================================
    # TRAINING SUMMARY TABLE 
    # ==========================================
    summary_df = pd.DataFrame(results_summary)



    
    print("\n" + "="*80)
    print("MASTER SUMMARY TABLE (ALL 9 RUNS)")
    print("="*80)
    # Configure pandas to display all columns cleanly in terminal
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    print(summary_df.to_string(index=False))
    print("="*80 + "\n")

    # ==========================================
    # MATPLOTLIB TRAINING VISUALIZATIONS
    # ==========================================

    # Plot the SSE over the number of iterations to see overall error trend for each set of initial weights and learning rate..

    # Will produce 4 graphs: A graph comparing runs 1-3, a graph comparing runs 4-6, a graph comparing runs 7-9, and a final graph comparing all 9 runs together.

    for idx, (cat_name, _) in enumerate(init_weight_categories):
        plt.figure(figsize=(9, 5))
        
        # idx 0 -> runs 1 to 3 | idx 1 -> runs 4 to 6 | idx 2 -> runs 7 to 9
        start_run = idx * 3 + 1
        end_run = start_run + 3
        
        for run_id in range(start_run, end_run):
            hist_data = all_histories[f"Run {run_id}"] # Extract from all_histories and plot
            plt.plot(hist_data["iters"], hist_data["sses_capped"], label=hist_data["label"], linewidth=2)


        # Log scale it so divergent errors don't dominate graph and make it hard to see the convergent ones.
        plt.yscale('log')
        plt.title(f"Training Loss Trajectory\n{cat_name}")
        plt.xlabel("Iterations")
        plt.ylabel("Sum of Squared Errors (SSE) [Log Scale]")
        plt.legend()
        plt.grid(True, which="both", ls="--", alpha=0.5)
        plt.tight_layout()
        
        # Save figure before showing
        filename = f"training_group_{idx + 1}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Saved: {filename}")
        plt.show()


    # Grand summary graph (all 9 runs)
    plt.figure(figsize=(11, 6))

    for run_id, hist_data in all_histories.items():
        plt.plot(hist_data["iters"], hist_data["sses_capped"], label=hist_data["label"], alpha=0.8, linewidth=1.5)

    # Log scale it so divergent errors don't dominate graph and make it hard to see the convergent ones.
    plt.yscale('log')
    plt.title("Grand Summary: All 9 Training Runs")
    plt.xlabel("Iterations")
    plt.ylabel("Sum of Squared Errors (SSE) [Log Scale]")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.tight_layout()

    # Save summary figure
    plt.savefig("summary_all_9_runs.png", dpi=300, bbox_inches='tight')
    print("Saved: summary_all_9_runs.png")
    plt.show()