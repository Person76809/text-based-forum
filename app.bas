DIM posts$(100) ' Array to store posts
DIM count ' Counter variable for number of posts

CLS ' Clear the screen

' Main program loop
DO
    PRINT "1. Create a new post"
    PRINT "2. View all posts"
    PRINT "3. Exit"
    INPUT "Enter your choice: ", choice

    SELECT CASE choice
        CASE 1
            INPUT "Enter your post: ", newPost$
            count = count + 1
            posts$(count) = newPost$
            PRINT "Post created!"
            PRINT
        CASE 2
            IF count = 0 THEN
                PRINT "No posts available."
                PRINT
            ELSE
                FOR i = 1 TO count
                    PRINT "Post " + STR$(i) + ": " + posts$(i)
                    PRINT
                NEXT i
            END IF
        CASE 3
            PRINT "Exiting..."
            END
        CASE ELSE
            PRINT "Invalid choice. Please try again."
            PRINT
    END SELECT
LOOP UNTIL choice = 3
