import networkx as nx


def elimination(file):
    # Read in information, establish data structures
    f = open(file, "r")
    digraph = nx.DiGraph()
    num_teams = int(f.readline())
    teams = []
    games = []
    g_vertices = []
    games_left = []

    # Pull information for teams vertices
    for i in range(num_teams):
        row = f.readline().split()
        teams.append((row[0], {"wins": int(row[1]),
                               "lost": int(row[2]),
                               "left": int(row[3])}))
        temp = row[4:]
        temp.insert(0, row[0])
        games.append(temp)

    s = 0
    i = 0
    j = 1
    for team in games:
        for team2 in games:
            # Pull information for game vertices
            if team != team2 and (team2[0] + "-" + team[0]) not in g_vertices:
                g_vertices.append(team[0] + "-" + team2[0])
                # Find games left between two teams
                games_left.append(int(games[i][j]))
                s += int(games[i][j])   # Source, total games left
            j += 1
        i += 1
        j = 1

    # Create all nodes from game vertices and team vertices lists
    digraph.add_node("Source", games=s)
    digraph.add_nodes_from(teams)
    digraph.add_nodes_from(g_vertices)
    digraph.add_node("Sink")

    i = 0
    for match in g_vertices:
        # Create edges from source to game vertices
        digraph.add_edge("Source", match, games=games_left[i])
        for team in teams:
            # Create edges from game vertices to team vertices
            if team[0] in match:
                digraph.add_edge(match, team[0])
        i += 1

    # Run through elimination to get edge weights for each team
    for team in teams:
        scenarios(digraph, teams, team, g_vertices)


def scenarios(digraph, teams, team_x, g_vertices):
    highest_wins = 0
    lead_team = ""
    flows = []  # List to hold flow_values

    # Scenario 1: Trivial Elimination
    for team in teams:
        if highest_wins < team[1]["wins"]:
            highest_wins = team[1]["wins"]
            lead_team = team[0]
    if (team_x[1]["wins"] + team_x[1]["left"]) < highest_wins:
        print(f"{team_x[0]} has been trivially eliminated by {lead_team}.")
        return

    # Scenario 2: Max Flow
    for team in teams:
        # Create edge weight between team vertices and Sink
        weight = team_x[1]["wins"] + team_x[1]["left"] - team[1]["wins"]
        digraph.add_edge(team[0], "Sink", capacity=weight)
        for edge in digraph.edges(g_vertices):
            if edge[1] == team[0]:
                nx.set_edge_attributes(digraph, {edge: {"capacity": weight}})
    # Create edge weight between game vertices and team vertices
    for edge in digraph.edges(g_vertices):
        flow_value, flow_dict = nx.maximum_flow(digraph, edge[0], edge[1])
        nx.set_edge_attributes(digraph, {edge: {"capacity": flow_value}})
        flows.append(flow_value)
    # If any flow_value is 0, the team has been eliminated
    # There is no possible way to reach Sink if flow_value is 0
    if 0 in flows:
        print(f"{team_x[0]} is eliminated.")
    else:
        print(f"{team_x[0]} is not eliminated.")


def main():
    files = ["mlb.txt", "potter.txt", "ivy_league.txt", "world_cup.txt"]
    for file in files:
        elimination(file)
        print()


if __name__ == "__main__":
    main()
