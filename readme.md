# Video

AI-assisted video production project for short brand and process videos, initially focused on [claudiaplessl.at](https://claudiaplessl.at).

Repository: [AINxtGenDev/video](https://github.com/AINxtGenDev/video).

## Project status

This repository currently contains planning and research notes. No application, video-generation integration, or automated production pipeline has been implemented.

[session.md](session.md) records the research session dated 4 November 2026, including proposed providers, costs, setup steps, and open questions. Treat those notes as historical research: model availability, pricing, technical capabilities, and legal conclusions require verification against current primary sources before use.

## Intended workflow

1. Confirm the production brief, source assets, and permission to use them.
2. Verify provider availability, current pricing, data handling, and suitable account settings.
3. Review any proposed CLI or integration before installation and configure credentials outside Git.
4. Agree on the prompt and spending limit before submitting a generation job.
5. Generate a draft, review its visual quality, and document the result and actual cost.
6. Produce approved versions and add voiceover, captions, or other finishing elements as needed.

Detailed proposals and unresolved questions are recorded in [session.md](session.md).

## Local repository

The initial working directory is `/home/nuc8/05_development/44_video`.

To clone using the project owner's SSH identity:

```bash
git -c core.sshCommand='ssh -i /home/nuc8/.ssh/github_werner -o IdentitiesOnly=yes -o StrictHostKeyChecking=yes' clone git@github.com:AINxtGenDev/video.git
cd video
git config --local core.sshCommand 'ssh -i /home/nuc8/.ssh/github_werner -o IdentitiesOnly=yes -o StrictHostKeyChecking=yes'
```

The key path is specific to that machine. Other contributors should use their own SSH identity and verify GitHub's host key before connecting.

## Credentials and generated assets

- Keep API credentials in local environment files or an appropriate secrets store. Never commit credentials or private keys.
- `.gitignore` excludes `.env` files, local Claude settings, common dependency/cache directories, and generated files under `outputs/` and `renders/`.
- Review staged changes before every commit, especially because this repository is public.
- Keep large generated media outside Git unless a deliberate storage strategy has been selected.

## References

- [Project research and proposed next steps](session.md).
- [GitHub: connecting with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).
- [GitHub: ignoring files](https://docs.github.com/en/get-started/git-basics/ignoring-files).

## License

No license has been selected for this project.
