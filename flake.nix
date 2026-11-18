{
  description = "Computerome wiki (Zensical) dev shell";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs =
    { nixpkgs, ... }:
    let
      forAllSystems = nixpkgs.lib.genAttrs nixpkgs.lib.systems.flakeExposed;
    in
    {
      devShells = forAllSystems (
        system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
        in
        {
          default = pkgs.mkShell {
            packages = [
              pkgs.python314
              pkgs.uv
              pkgs.pngquant
            ];
            UV_PYTHON = "${pkgs.python314}/bin/python";
            UV_PYTHON_DOWNLOADS = "never";
          };
        }
      );
    };
}
