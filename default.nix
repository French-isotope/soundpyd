let pkgs = import ./nixpkgs.nix {};
  pythonEnv = pkgs.python3.withPackages(p : [p.numpy p.matplotlib]);
in pkgs.mkShell {
  buildInputs = [ pythonEnv ];
}
