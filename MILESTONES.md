# Flash-Decks Development Milestones

This document outlines the progressive milestones for building out the minimal flashcards application into a full-featured learning platform. Students will start with `minimal-flashcards` (basic version) and incrementally add features to match `flashcards-app` (full version) using Claude Code as their development assistant.

## Learning Objectives

By completing these milestones, students will:
- Build and extend a full-stack web application using modern frameworks
- Understand and implement complex features with AI assistance
- Learn containerization and deployment practices
- Integrate local and cloud-based LLM services
- Apply software testing and CI/CD principles
- Make architectural decisions balancing functionality and maintainability

---

## Milestone 0: Foundation & Environment Setup

**Goal**: Understand the existing codebase and establish a working local development environment.

**Learning Objectives**:
- Navigate and understand a monorepo structure
- Set up local development tools (Python, Node.js, PostgreSQL)
- Run frontend and backend services independently
- Understand the basic data model and API structure

**Technical Tasks**:
1. Clone the `minimal-flashcards` repository
2. Set up Python virtual environment and install backend dependencies
3. Set up Node.js environment and install frontend dependencies
4. Configure PostgreSQL database (local or Docker container)
5. Run database migrations with Alembic
6. Start backend server and verify API docs at `/docs`
7. Start frontend dev server and verify basic functionality
8. Create a test user and explore the application features

**Success Criteria**:
- [ ] Backend running on `http://localhost:8000` with API documentation accessible
- [ ] Frontend running on `http://localhost:5173` with working UI
- [ ] Can create an account, log in, create decks, add cards, and start a study session
- [ ] Database persists data correctly across server restarts
- [ ] Can explain the request flow from frontend → backend → database

**Estimated Complexity**: ⭐⭐ (Medium - setup issues are common)

**Claude Code Tips**:
- Use Claude to explain the codebase structure and architecture
- Ask Claude to help debug environment setup issues
- Have Claude walk through the authentication flow and API endpoints

---

## Milestone 1: Docker Foundation

**Goal**: Containerize the application components for consistent deployment and understand Docker fundamentals.

**Learning Objectives**:
- Understand Docker containers vs. local development
- Write Dockerfiles for different application components
- Use docker-compose to orchestrate multi-container applications
- Design for both local and containerized execution

**Technical Tasks**:
1. Create `Dockerfile` for backend service
   - Use Python 3.11+ base image
   - Install dependencies from requirements.txt
   - Configure for production (uvicorn without reload)
2. Create `Dockerfile` for frontend service
   - Use Node.js base image for build
   - Use nginx for serving static files
3. Create `docker-compose.yml` for the full stack
   - PostgreSQL service with persistent volume
   - Backend service with database connection
   - Frontend service with backend API proxy
   - Network configuration for inter-service communication
4. Add environment variable configuration (`.env.docker`)
5. Test the application running entirely in Docker
6. Ensure the app still runs locally without Docker

**Success Criteria**:
- [ ] `docker-compose up` starts all services successfully
- [ ] Application accessible and fully functional via Docker setup
- [ ] Database data persists across container restarts (volumes configured)
- [ ] Application still runs in local development mode
- [ ] Environment variables properly configured for both modes

**Estimated Complexity**: ⭐⭐⭐ (Medium-High - Docker networking can be tricky)

**Claude Code Tips**:
- Ask Claude to generate Dockerfiles optimized for each service
- Have Claude explain Docker networking and volume mounting
- Use Claude to troubleshoot container communication issues

**Reference**: See `flashcards-app/docker/` for examples

---

## Milestone 2: UI Enhancement - Tailwind CSS Migration

**Goal**: Upgrade the styling framework from basic CSS to Tailwind CSS for better maintainability and design consistency.

**Learning Objectives**:
- Understand utility-first CSS frameworks
- Migrate existing styles to Tailwind conventions
- Design responsive layouts with Tailwind
- Configure build tools for CSS processing

**Technical Tasks**:
1. Install Tailwind CSS and its dependencies
   ```bash
   npm install -D tailwindcss postcss autoprefixer
   ```
2. Initialize Tailwind configuration (`tailwind.config.ts`)
3. Configure PostCSS (`postcss.config.js`)
4. Update `index.css` with Tailwind directives
5. Migrate landing page styles to Tailwind utilities
6. Migrate dashboard page styles to Tailwind utilities
7. Migrate deck detail and study session pages
8. Create reusable component classes for buttons, cards, forms
9. Add dark mode support (optional stretch)
10. Ensure responsive design on mobile devices

**Success Criteria**:
- [ ] All pages styled with Tailwind CSS utilities
- [ ] No custom CSS files remaining (except Tailwind config)
- [ ] Consistent design language across all pages
- [ ] Responsive layouts work on mobile, tablet, and desktop
- [ ] Build process includes Tailwind CSS compilation
- [ ] Application visual quality matches or exceeds original styling

**Estimated Complexity**: ⭐⭐ (Medium - mostly mechanical refactoring)

**Claude Code Tips**:
- Ask Claude to convert specific CSS blocks to Tailwind utilities
- Have Claude suggest Tailwind patterns for common components
- Use Claude to ensure accessibility is maintained during migration

**Reference**: Compare `minimal-flashcards` CSS with `flashcards-app` Tailwind usage

---

## Milestone 3: Advanced Card Types

**Goal**: Expand beyond basic flashcards to support multiple question types (multiple choice, short answer, cloze deletion).

**Learning Objectives**:
- Extend database schema with migrations
- Handle polymorphic data structures (different card types)
- Build type-specific UI components
- Validate and serialize complex data types

**Technical Tasks**:

### Backend:
1. Update `Card` model to support `options_json` field for MCQ options
2. Add validation for different card types in `CardCreate` schema
3. Update `decks.py` service to handle card type-specific logic
4. Create Alembic migration for schema changes
5. Add API endpoints for card type-specific operations

### Frontend:
1. Create `MultipleChoiceCard.tsx` component
   - Display 4 options (A, B, C, D)
   - Handle option selection
   - Show correct answer on reveal
2. Create `ShortAnswerCard.tsx` component
   - Text input for user answer
   - Display expected answer(s) on reveal
   - Self-grading buttons (Correct/Incorrect)
3. Create `ClozeCard.tsx` component
   - Parse `{{c1::hidden text}}` syntax
   - Show blanks initially
   - Reveal hidden text on flip
4. Update `StudySessionPage.tsx` to render appropriate card type
5. Update deck creation/editing UI to specify card type
6. Add card type icons and labels throughout the UI

**Success Criteria**:
- [ ] Database schema supports all four card types (basic, multiple_choice, short_answer, cloze)
- [ ] Can create cards of each type through the UI
- [ ] Study sessions correctly render each card type
- [ ] MCQ cards validate correct answer selection
- [ ] Short answer cards display expected answer
- [ ] Cloze cards parse and display blanks correctly
- [ ] Card type is visible in deck detail view

**Estimated Complexity**: ⭐⭐⭐ (Medium-High - requires both backend and frontend changes)

**Claude Code Tips**:
- Ask Claude to generate the database migration for new fields
- Have Claude implement type-specific validation logic
- Use Claude to create component templates for each card type

**Reference**: See `flashcards-app/app/models/card.py` and card components

---

## Milestone 4: Study Mode Enhancements

**Goal**: Add exam mode with timer and scoring, practice mode options, and card flagging system.

**Learning Objectives**:
- Implement session state management
- Build timer functionality with React hooks
- Create summary/results screens
- Add user feedback mechanisms (flagging)

**Technical Tasks**:

### Exam Mode:
1. Add `exam` mode to `StudyMode` enum
2. Create `ExamSession` configuration (time limit, question count)
3. Implement countdown timer in frontend
4. Add final score calculation and summary screen
5. Store exam results with timestamp and score

### Practice Mode Options:
1. Add configurable practice session options:
   - Number of cards (or "Endless")
   - Random shuffle vs. sequential
   - Include flagged cards only
2. Update session creation UI with mode selector
3. Implement practice mode logic in backend

### Card Flagging:
1. Create `FlaggedCard` model (user_id, card_id, reason, flagged_at)
2. Add API endpoints for flagging/unflagging cards
   - `POST /cards/{card_id}/flag`
   - `DELETE /cards/{card_id}/flag`
3. Add flag icon button to study session UI
4. Show flagged cards with indicator in deck detail
5. Add "Review Flagged Cards" option in practice mode

**Success Criteria**:
- [ ] Exam mode starts with countdown timer
- [ ] Timer displays remaining time and warns when running low
- [ ] Exam ends automatically when time expires or all cards answered
- [ ] Final score screen shows percentage, time taken, and per-card results
- [ ] Practice mode allows customization (card count, shuffle)
- [ ] Can flag/unflag cards during study sessions
- [ ] Flagged cards visible in deck detail with flag indicator
- [ ] Can start practice session with only flagged cards

**Estimated Complexity**: ⭐⭐⭐⭐ (High - complex state management)

**Claude Code Tips**:
- Ask Claude to implement the countdown timer with pause/resume functionality
- Have Claude design the exam summary UI with statistics
- Use Claude to handle edge cases (timer running out, page refresh)

**Reference**: See `flashcards-app/EXAM_MODE_DOCUMENTATION.md` and `FlaggedCard` model

---

## Milestone 5: Spaced Repetition System (SRS)

**Goal**: Implement the SM-2 spaced repetition algorithm for optimized long-term learning.

**Learning Objectives**:
- Understand spaced repetition principles and SM-2 algorithm
- Implement scheduling algorithms
- Track per-user, per-card learning state
- Build due card queue system

**Technical Tasks**:

### Backend (SM-2 Algorithm):
1. Verify `SRSReview` model exists with fields:
   - `repetitions`, `interval_days`, `easiness`, `due_at`, `last_quality`
2. Implement SM-2 update logic in `study.py` service:
   ```
   If quality < 3: reset (n=0, I=1)
   Else if n=0: n=1, I=1
   Else if n=1: n=2, I=6
   Else: I = round(I * E)
   E = max(1.3, E + (0.1 - (5-Q) * (0.08 + (5-Q) * 0.02)))
   due_at = now + I days
   ```
3. Create `GET /reviews/due` endpoint to fetch cards due for review
4. Update session answer submission to calculate next review date
5. Add streak calculation logic (consecutive days studied)

### Frontend:
1. Add "Review" study mode with quality grading (1-5 buttons)
2. Show review queue count on dashboard ("X cards due today")
3. Display next review date for each card in deck detail
4. Add study heatmap visualization (git-style calendar)
5. Show streak counter on dashboard
6. Add progress indicators (new/learning/review counts per deck)

**Success Criteria**:
- [ ] SRS scheduling state persists per user per card
- [ ] Quality ratings (1-5) correctly update intervals using SM-2
- [ ] Cards rated < 3 reset to beginning of learning cycle
- [ ] Dashboard shows accurate count of due cards
- [ ] Review mode only shows cards due today or overdue
- [ ] Streak counter increments on consecutive study days
- [ ] Study heatmap visualizes activity over time
- [ ] Deck progress shows distribution (new/learning/review)

**Estimated Complexity**: ⭐⭐⭐⭐ (High - complex algorithm and state tracking)

**Claude Code Tips**:
- Ask Claude to implement and explain the SM-2 algorithm
- Have Claude write unit tests for the scheduling logic
- Use Claude to create the heatmap visualization component

**Reference**: See `flashcards-app/app/services/study.py` SM-2 implementation

---

## Milestone 6: Testing & Quality Assurance

**Goal**: Achieve comprehensive test coverage for both backend and frontend with automated testing.

**Learning Objectives**:
- Write unit tests and integration tests
- Use pytest fixtures and mocking
- Test React components with Testing Library
- Understand test-driven development principles

**Technical Tasks**:

### Backend Testing (pytest):
1. Set up pytest with coverage reporting
2. Write unit tests for services:
   - Auth service (password hashing, token generation)
   - Deck service (CRUD operations)
   - Study service (SM-2 algorithm, session management)
   - SRS calculation edge cases
3. Write integration tests for API endpoints:
   - Auth endpoints (signup, login, logout, refresh)
   - Deck endpoints (create, update, delete, list)
   - Study session endpoints (create, answer, finish)
   - Review endpoints (due cards)
4. Add test fixtures for database setup/teardown
5. Mock external dependencies (if any)
6. Achieve 80%+ test coverage

### Frontend Testing (Vitest):
1. Set up Vitest with React Testing Library
2. Write component tests:
   - `Flashcard.tsx` (flip animation, answer reveal)
   - `MultipleChoiceCard.tsx` (option selection)
   - `DeckCard.tsx` (rendering, click handlers)
3. Write store tests:
   - `authStore.ts` (login, logout, token refresh)
4. Write integration tests:
   - Login flow
   - Deck creation flow
   - Study session flow
5. Add API mocking with MSW (Mock Service Worker)
6. Achieve 70%+ test coverage for critical components

**Success Criteria**:
- [ ] Backend: 80%+ test coverage with passing tests
- [ ] Frontend: 70%+ test coverage for components and stores
- [ ] All critical user flows covered by integration tests
- [ ] Tests run successfully in CI environment
- [ ] Test commands documented in README
- [ ] No flaky tests (tests pass consistently)

**Estimated Complexity**: ⭐⭐⭐⭐ (High - requires testing discipline)

**Claude Code Tips**:
- Ask Claude to generate test cases for specific functions
- Have Claude write fixtures and mocks for complex scenarios
- Use Claude to improve test coverage for low-coverage areas

**Reference**: See `flashcards-app/backend/tests/` and `flashcards-app/TEST_GUIDE.md`

---

## Milestone 7: LLM Integration (Stretch Goal)

**Goal**: Integrate both local (Ollama) and cloud (OpenAI/Anthropic) LLMs for AI-powered deck generation and answer checking.

**Learning Objectives**:
- Integrate with local LLM services (Ollama)
- Use cloud LLM APIs (OpenAI, Anthropic)
- Design abstraction layers for multiple LLM providers
- Implement prompt engineering for consistent outputs
- Parse and ingest documents (PDF, PPTX, DOCX)

**Technical Tasks**:

### Phase 1: LLM Service Abstraction
1. Install dependencies:
   ```bash
   pip install openai ollama PyPDF2 python-pptx python-docx
   ```
2. Create `llm_service.py` with provider abstraction:
   - `generate_with_openai(prompt, model)`
   - `generate_with_ollama(prompt, model)`
   - `generate_flashcards(text, question_types, count)`
3. Add environment variable support:
   - `OPENAI_API_KEY` (for OpenAI)
   - `ANTHROPIC_API_KEY` (for Claude)
   - `OLLAMA_BASE_URL` (default: `http://localhost:11434`)
4. Implement provider selection logic (try local first, fallback to API)

### Phase 2: Document Parsing
1. Create `file_parser.py` service:
   - `parse_pdf(file)` using PyPDF2
   - `parse_pptx(file)` using python-pptx
   - `parse_docx(file)` using python-docx
2. Extract text content from uploaded documents
3. Handle errors gracefully (corrupted files, unsupported formats)

### Phase 3: AI Deck Generation
1. Create `POST /ai/generate` endpoint
   - Accept text input or file upload
   - Accept parameters (question types, count)
2. Design prompts for each question type:
   - Basic Q&A format
   - Multiple choice with 4 options
   - Short answer with expected answers
   - Cloze deletion with `{{c1::}}` syntax
3. Parse LLM JSON responses into card format
4. Create deck and cards in database
5. Return generated deck ID

### Phase 4: AI Answer Checking
1. Create `POST /ai/check-answer` endpoint
   - Accept user answer and expected answer
   - Return correctness score and feedback
2. Implement semantic answer comparison
3. Integrate into study session for short answer cards
4. Show AI feedback in study session UI

### Frontend:
1. Create `AIPoweredDecksPage.tsx`:
   - Text input for content
   - File upload for PDF/PPTX/DOCX
   - Question type selectors (checkboxes)
   - Card count slider
   - LLM provider selector (local/OpenAI/Claude)
   - Generate button with loading state
2. Show generation progress and preview
3. Allow editing generated cards before saving
4. Integrate AI answer checking in short answer cards

**Success Criteria**:
- [ ] Ollama running locally with a model (e.g., Llama 3)
- [ ] Can generate flashcards using Ollama (local)
- [ ] Can generate flashcards using OpenAI API (with API key)
- [ ] Can upload PDF/PPTX/DOCX and extract text
- [ ] Generated cards include all four question types
- [ ] AI feedback on short answer questions is helpful and accurate
- [ ] LLM provider is selectable in UI
- [ ] Graceful fallback when local LLM unavailable
- [ ] Cost-effective: prioritizes local LLM, uses API as backup

**Estimated Complexity**: ⭐⭐⭐⭐⭐ (Very High - multiple integrations, prompt engineering)

**Claude Code Tips**:
- Ask Claude to help with Ollama setup and model selection
- Have Claude design robust prompts for each card type
- Use Claude to implement error handling for LLM timeouts/failures
- Ask Claude to explain the trade-offs between local and cloud LLMs

**Reference**:
- `flashcards-app/app/services/llm_service.py`
- `flashcards-app/AI_DECK_GENERATION_SUMMARY.md`
- `flashcards-app/QUICK_REFERENCE.md`

---

## Milestone 8: CI/CD Pipeline

**Goal**: Set up continuous integration and continuous deployment for automated testing and deployment.

**Learning Objectives**:
- Configure GitHub Actions workflows
- Run tests in CI environment
- Build and publish Docker images
- Understand deployment pipelines

**Technical Tasks**:

1. Create `.github/workflows/ci.yml`:
   - Run on push and pull request
   - Set up Python 3.11 environment
   - Set up Node.js 18 environment
   - Start PostgreSQL service
   - Run backend tests with coverage
   - Run frontend tests with coverage
   - Build Docker images
   - Lint code (ESLint, Black/Ruff)

2. Add code quality checks:
   - Backend: Black (formatting), Ruff (linting)
   - Frontend: ESLint, Prettier
   - Type checking: mypy (Python), tsc (TypeScript)

3. Set up test database for CI:
   - Use PostgreSQL service in GitHub Actions
   - Run migrations before tests
   - Seed test data

4. Add badges to README:
   - Build status
   - Test coverage
   - Code quality

5. (Optional) Set up deployment:
   - Deploy to staging environment on merge to `main`
   - Deploy to production on release tag
   - Use platforms like Railway, Fly.io, or AWS

**Success Criteria**:
- [ ] CI pipeline runs on every push and PR
- [ ] All tests pass in CI environment
- [ ] Docker images build successfully
- [ ] Code quality checks enforce standards
- [ ] Coverage reports generated and tracked
- [ ] README displays CI status badges
- [ ] (Optional) Automatic deployment to staging

**Estimated Complexity**: ⭐⭐⭐ (Medium-High - CI config can be finicky)

**Claude Code Tips**:
- Ask Claude to generate GitHub Actions workflow files
- Have Claude troubleshoot CI failures and environment issues
- Use Claude to set up deployment configurations

**Reference**: See `flashcards-app/.github/workflows/ci.yml`

---

## Milestone 9: Production Readiness & Deployment

**Goal**: Prepare the application for production deployment with proper configuration, security, and monitoring.

**Learning Objectives**:
- Configure production environments
- Implement security best practices
- Set up logging and monitoring
- Deploy to cloud platforms

**Technical Tasks**:

### Security Hardening:
1. Review and update JWT secret keys (use strong random values)
2. Enable HTTPS in production (SSL/TLS certificates)
3. Configure CORS for production domains only
4. Add rate limiting for auth endpoints
5. Sanitize user inputs to prevent XSS/SQL injection
6. Add Content Security Policy headers
7. Enable secure cookie flags (`Secure`, `HttpOnly`, `SameSite`)

### Configuration Management:
1. Create separate `.env` files for dev, staging, production
2. Use environment-specific database URLs
3. Configure production-optimized settings:
   - Disable debug mode
   - Set appropriate timeouts
   - Configure connection pooling
4. Document all required environment variables

### Logging & Monitoring:
1. Configure structured logging with Loguru
2. Add request ID tracking for distributed tracing
3. Log authentication events (login, logout, failures)
4. Set up error tracking (optional: Sentry integration)
5. Add health check endpoint (`/health`)
6. Monitor database connection health

### Deployment:
1. Choose deployment platform (Railway, Fly.io, AWS, etc.)
2. Deploy PostgreSQL database (managed service recommended)
3. Deploy backend service with environment variables
4. Deploy frontend with backend API URL configured
5. Set up domain name and SSL certificate
6. Test deployed application end-to-end
7. Document deployment process

**Success Criteria**:
- [ ] Application runs securely in production environment
- [ ] HTTPS enabled with valid SSL certificate
- [ ] Environment variables properly configured for production
- [ ] Logging captures important events and errors
- [ ] Health check endpoint returns status
- [ ] Database is backed up regularly
- [ ] Application is accessible via public domain
- [ ] Documentation includes deployment instructions

**Estimated Complexity**: ⭐⭐⭐⭐ (High - many moving parts)

**Claude Code Tips**:
- Ask Claude to review security checklist for production
- Have Claude generate deployment configuration files
- Use Claude to troubleshoot deployment issues

**Reference**: See `flashcards-app/docker/` for production Docker setup

---

## Milestone 10: Final Polish & Documentation

**Goal**: Refine the user experience, complete documentation, and prepare for handoff.

**Learning Objectives**:
- Write comprehensive documentation
- Conduct user experience improvements
- Create demo content
- Prepare for knowledge transfer

**Technical Tasks**:

### UX Improvements:
1. Add loading states and skeleton screens
2. Improve error messages and validation feedback
3. Add keyboard shortcuts (space=flip, arrows=navigate, 1-5=grade)
4. Implement autosave for study sessions
5. Add confirmation dialogs for destructive actions
6. Improve mobile responsiveness
7. Add accessibility features (ARIA labels, focus management)

### Documentation:
1. Write comprehensive `README.md`:
   - Project overview and features
   - Setup instructions (local and Docker)
   - Architecture diagram
   - API documentation
   - Testing guide
2. Create `ARCHITECTURE.md` documenting design decisions
3. Create `DEPLOYMENT.md` with step-by-step deployment guide
4. Add inline code comments for complex logic
5. Create user guide with screenshots
6. Document known issues and limitations

### Demo Content:
1. Create sample decks for demonstration:
   - Computer Science (algorithms, data structures)
   - Math (algebra, calculus)
   - Language Learning (vocabulary, grammar)
2. Pre-seed database with demo content
3. Create video walkthrough of features (optional)
4. Prepare presentation slides (optional)

### Code Quality:
1. Refactor duplicated code into reusable functions
2. Ensure consistent code style across codebase
3. Remove unused dependencies
4. Optimize bundle size (frontend)
5. Review and clean up commented code
6. Final code review pass

**Success Criteria**:
- [ ] Application is polished and user-friendly
- [ ] All features work smoothly without bugs
- [ ] Documentation is complete and accurate
- [ ] Demo content showcases key features
- [ ] Code is clean, well-organized, and commented
- [ ] Application is ready for production use
- [ ] Handoff materials prepared (if applicable)

**Estimated Complexity**: ⭐⭐⭐ (Medium-High - attention to detail)

**Claude Code Tips**:
- Ask Claude to review documentation for clarity and completeness
- Have Claude suggest UX improvements based on user flows
- Use Claude to generate demo content and sample data

---

## Recommended Milestone Order

### Minimum Viable Product (MVP):
1. Milestone 0: Foundation & Environment Setup
2. Milestone 1: Docker Foundation
3. Milestone 2: UI Enhancement - Tailwind CSS Migration
4. Milestone 3: Advanced Card Types
5. Milestone 6: Testing & Quality Assurance (basic tests)

### Enhanced Product:
6. Milestone 4: Study Mode Enhancements
7. Milestone 5: Spaced Repetition System
8. Milestone 6: Testing & Quality Assurance (comprehensive)
9. Milestone 8: CI/CD Pipeline

### Advanced Features (Stretch):
10. Milestone 7: LLM Integration
11. Milestone 9: Production Readiness & Deployment
12. Milestone 10: Final Polish & Documentation

---

## Using Claude Code Effectively

### Best Practices:
1. **Start with Understanding**: Ask Claude to explain code before modifying it
2. **Incremental Changes**: Implement features in small, testable increments
3. **Test As You Go**: Write tests alongside feature implementation
4. **Document Decisions**: Ask Claude to document why certain approaches were chosen
5. **Review Generated Code**: Always review and understand Claude's suggestions
6. **Ask "Why"**: When Claude suggests something, ask for the rationale
7. **Iterate**: Don't expect perfection on the first try; iterate and refine

### Example Claude Code Prompts:
- "Explain the authentication flow in this codebase"
- "Help me implement the SM-2 algorithm for spaced repetition"
- "Generate a Dockerfile for the FastAPI backend with best practices"
- "Write pytest tests for the deck CRUD operations"
- "Convert this CSS file to Tailwind utility classes"
- "Review this code for security vulnerabilities"
- "Help me debug why the timer isn't counting down correctly"

### When to Ask Claude:
- ✅ Understanding existing code architecture
- ✅ Implementing well-defined features
- ✅ Writing tests and documentation
- ✅ Debugging specific errors
- ✅ Optimizing performance
- ✅ Security review and best practices

### When to Do It Yourself:
- ⚠️ Making high-level architectural decisions
- ⚠️ Choosing technologies for specific use cases
- ⚠️ Understanding core concepts (don't just copy-paste)
- ⚠️ Final review before deployment

---

## Assessment Rubric

Each milestone can be evaluated on:

1. **Functionality** (40%)
   - All features work as specified
   - No critical bugs
   - Edge cases handled

2. **Code Quality** (25%)
   - Clean, readable code
   - Proper separation of concerns
   - Consistent style
   - Appropriate comments

3. **Testing** (15%)
   - Adequate test coverage
   - Tests pass reliably
   - Both unit and integration tests

4. **Documentation** (10%)
   - Clear README
   - Code comments where needed
   - Setup instructions work

5. **Understanding** (10%)
   - Can explain design decisions
   - Understands trade-offs
   - Can answer questions about implementation

---

## Additional Resources

- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **React Documentation**: https://react.dev/
- **Tailwind CSS**: https://tailwindcss.com/docs
- **Docker Documentation**: https://docs.docker.com/
- **Ollama**: https://ollama.ai/
- **OpenAI API**: https://platform.openai.com/docs
- **PostgreSQL**: https://www.postgresql.org/docs/
- **pytest**: https://docs.pytest.org/
- **Vitest**: https://vitest.dev/

---

## Support

For questions or issues:
1. Refer to `CLAUDE.md` for architecture guidance
2. Use Claude Code to explain specific code sections
3. Check the reference implementation in `flashcards-app/`
4. Contact course staff (see POCs in main README)

Good luck building! 🚀
