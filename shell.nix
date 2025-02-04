let pkgs = import <nixpkgs> { };
in pkgs.mkShell {
  packages = with pkgs; [
    git
    python3
    ollama
    curl
  ];
}
