# Step 1: Navigate to the right location

  - cd ~/.ssh

# Step 2: Create the SSH keys

  - ssh-keygen -t rsa -C "email"
  - hit enter
  - It will prompt you for a file name, you should name it something like:
      - id_rsa_[tag]

# Step 3: Create a config file

  - try ls -> to list if config file exists
  - if it does -> open in code -> code config
  - if it doesn't -> touch config
  - add lines

    - # Personal account

      Host github.com
      HostName github.com
      IdentityFile ~/.ssh/id_rsa_[tag]
      User git
      IdentitiesOnly yes

# Step 4: Add keys to your accounts

  - cat id_rsa_[tag].pub
  - navigate to the SSH/GPG keys section of Github and paste your new key.

# Step 5: “Too Open” Error

  - chmod 600 ~/.ssh/id_rsa_[tag]

# Test connection (github)

  - ssh -T git@github.com
  - yes

# Add Identity

  - ssh-add ~/.ssh/id_rsa_[tag]

# Add remote-origin

  - git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
